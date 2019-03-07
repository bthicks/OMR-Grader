import os
import sys
import argparse
import base64
import json
import math

import cv2 as cv
from imutils.perspective import four_point_transform
import pyzbar.pyzbar as pyzbar
import numpy as np 

import fifty_questions
import short_answer


class Grader:

    def find_page(self, im):
        """
        Finds and returns the test box within a given image.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.

        Returns:
            numpy.ndarray: An ndarray representing the test box in the image.

        """
        # Convert image to grayscale then blur to better detect contours.
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(imgray.copy(), (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

        # Find contour for entire page. 
        _, contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        if (len(contours) > 0):
            # Approximate the contour.
            for contour in contours:
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)

                # Verify that contour has four corners.
                if (len(approx) == 4):
                    page = approx
                    break 
        else:
            return None

        # Apply perspective transform to get top down view of page.
        return four_point_transform(imgray, page.reshape(4, 2))

    def decode_qr(self, im): 
        """
        Finds and decodes the QR code inside of a test image.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.

        Returns:
            pyzbar.Decoded: A decoded QR code object.

        """
        # Increase image contrast to better identify QR code.
        _, new_page = cv.threshold(im, 127, 255, cv.THRESH_BINARY)

        decoded_objects = pyzbar.decode(new_page)

        if (decoded_objects == []):
            return None
        else:
            return decoded_objects[0]

    def rotate_image(self, im, angle):
        """
        Rotates an image by a specified angle.

        Args:
            im (numpy.ndarray): An ndarray representing the entire test image.
            angle (int): The angle, in degrees, by which the image should be 
                rotated.

        Returns:
            numpy.ndarray: An ndarray representing the rotated test image.

        """
        w = im.shape[1]
        h = im.shape[0]
        rads = np.deg2rad(angle)

        # Calculate new image width and height.
        nw = abs(np.sin(rads) * h) + abs(np.cos(rads) * w)
        nh = abs(np.cos(rads) * h) + abs(np.sin(rads) * w)

        # Get the rotation matrix.
        rot_mat = cv.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, 1)

        # Calculate the move from old center to new center combined with the 
        # rotation.
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))

        # Update the translation of the transform.
        rot_mat[0,2] += rot_move[0]
        rot_mat[1,2] += rot_move[1]

        return cv.warpAffine(im, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv.INTER_LANCZOS4)

    def image_is_upright(self, page):
        """
        Checks if an image is upright, based on the coordinates of the QR code
        in the image

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            bool: True if image is upright, False otherwise.

        """
        qr_code = self.decode_qr(page)
        qr_x = qr_code.rect.left
        qr_y = qr_code.rect.top
        qr_h = qr_code.rect.height
        w = page.shape[1]
        h = page.shape[0]

        if (0 <= qr_x <= (w / 4) and (h / 2) <= qr_y <= h):
            return True
        else:
            return False

    def upright_image(self, page):
        """
        Rotates an image by 90 degree increments until it is upright.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            page (numpy.ndarray): An ndarray representing the upright test 
                image.

        """
        if (self.image_is_upright(page)):
            return page
        else:
            for _ in range(3):
                page = self.rotate_image(page, 90)
                if (self.image_is_upright(page)):
                    return page
        return None

    def scale_config(self, config, width, height):
        """
        Scales the values in the config dictionary based on the width and height
        of the image being graded.

        Args:
            config (dict): An unscaled coordinate mapping read from the 
                configuration file.
            width (int): Width of the actual test image.
            height (int): Height of the actual test image.

        Returns:
            config (dict): A scaled coordinate mapping read from the 
                configuration file. 

        """
        x_scale = width / config['page_width']
        y_scale = height / config['page_height']

        for key, val in config.items():
            if 'x' in key or key == 'bubble_width':
                config[key] = val * x_scale
            elif 'y' in key or key == 'bubble_height':
                config[key] = val * y_scale

        return config

    def encode_image(self, image):
        """
        Encodes a .png image into a base64 string.

        Args:
            image (numpy.ndarray): An ndarray representing an image.

        Returns:
            str: A base64 string encoding of the image.

        """
        if (image is None):
            return None
        else:
            _, binary = cv.imencode('.png', image)
            encoded = base64.b64encode(binary)
            return encoded.decode("utf-8")

    def grade(self, image_name, verbose_mode, debug_mode):
        """
        Grades a test image and outputs the result to stdout as a JSON object.

        Args:
            image_name (str): Filepath to the test image to be graded.

        """
        # For testing.
        if (debug_mode):
            cv.namedWindow(image_name, cv.WINDOW_NORMAL)
            cv.resizeWindow(image_name, 850, 1100)

        # Initialize dictionary to be returned.
        data = {
            'answers' : {
                'bubbled' : [],
                'unsure' : [],
                'images' : [],
                'status' : 0
            },
            'version' : {
                'bubbled' : [],
                'image' : '',
                'status' : 0
            },
            'id' : {
                'bubbled' : [],
                'unsure' : [],
                'images' : [],
                'status' : 0
            },
            'status' : 0,
            'error' : ''
        }

        # Load image. 
        im = cv.imread(image_name)
        if (im is None):
            data['status'] = 1
            data['error'] = 'Image', image_name, 'not found'
            return json.dump(data, sys.stdout);

        # Find test page within image.
        page = self.find_page(im)
        if (page is None):
            data['status'] = 1
            data['error'] = 'Page not found in', image_name
            return json.dump(data, sys.stdout);

        # Decode QR code, which will contain path to configuration file.
        qr_code = self.decode_qr(page)
        if (qr_code is None):
            data['status'] = 1
            data['error'] = 'QR code not found'
            return json.dump(data, sys.stdout);
        else:
            qr_data = qr_code.data.decode('utf-8')
            qr_data = os.path.dirname(os.path.abspath(sys.argv[0]))+'/config/6q.json'

        # Read config file into dictionary and scale values.
        try:
            with open(os.path.dirname(os.path.abspath(sys.argv[0]))+'/config/6q.json') as file:
                config = json.load(file)
            config = self.scale_config(config, page.shape[1], page.shape[0])
        except FileNotFoundError:
            data['status'] = 1
            data['error'] = 'Configuration file', qrData, 'not found'
            return json.dump(data, sys.stdout);

        # Rotate page until upright.
        page = self.upright_image(page)
        if (page is None):
            data['status'] = 1
            data['error'] = 'Could not upright page in', image_name
            return json.dump(data, sys.stdout);

        # Create test object.
        test = short_answer.ShortAnswerTest(page, config, verbose_mode)

        # Find answers box and grade bubbles.
        answer_box = test.get_answer_box()
        if (answer_box is None):
            data['status'] = 1
            data['error'] = 'Answer box not found'
        else:
            answer_data = test.grade_answers(answer_box)

            data['answers']['bubbled'] = answer_data[0]
            data['answers']['unsure'] = answer_data[1]
            data['answers']['status'] = answer_data[3]

            for image in answer_data[2]:
                data['answers']['images'].append(self.encode_image(image))

                if (debug_mode):
                    cv.imshow(image_name, image)
                    cv.waitKey()

        # Find version box and grade bubbles.
        version_box = test.get_version_box()
        if version_box is None:
            data['status'] = 1
            data['error'] = 'Version box not found'
        else:
            version_data = test.grade_version(version_box)

            data['version']['bubbled'] = version_data[0]
            data['version']['image'] = self.encode_image(version_data[1])
            data['version']['status'] = version_data[2]

            if (debug_mode and version_data[1] is not None):
                cv.imshow(image_name, version_data[1])
                cv.waitKey()

        # Find id box and grade bubbles.
        id_box = test.get_id_box()
        if (id_box is None):
            data['status'] = 1
            data['error'] = 'ID box not found'
        else:
            id_data = test.grade_id(id_box)

            data['id']['bubbled'] = id_data[0]
            data['id']['unsure'] = id_data[1]
            data['id']['status'] = id_data[3]

            for image in id_data[2]:
                data['id']['images'].append(self.encode_image(image))

                if (debug_mode):
                    cv.imshow(image_name, image)
                    cv.waitKey()

        # Output result as a JSON object to stdout.
        json.dump(data, sys.stdout)
        
        # For testing.
        #return json.dumps(data)


def main():
    """
    Parses command line arguments and grades the specified test.

    """
    # Parse the arguments.
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, help='path to the input image')
    ap.add_argument('-v', action='store_true', required=False, help='enable verbose mode')
    ap.add_argument('-d', action='store_true', required=False, help='enable debug mode')
    args = vars(ap.parse_args())

    # Grade test.
    grader = Grader()
    return grader.grade(args['image'], args['v'], args['d'])

if __name__ == '__main__':
    main()
