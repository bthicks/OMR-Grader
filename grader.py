import os
import sys
import argparse
import json
import re

import cv2 as cv
from imutils.perspective import four_point_transform
import pyzbar.pyzbar as pyzbar

import config_parser
from test_box import TestBox
import utils


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
        threshold = utils.get_threshold(imgray)

        # Find contour for entire page. 
        contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, 
            cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        if len(contours) > 0:
            # Approximate the contour.
            for contour in contours:
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)

                # Verify that contour has four corners.
                if len(approx) == 4:
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

        if not decoded_objects:
            return None
        else:
            return decoded_objects[0]

    def image_is_upright(self, page, config):
        """
        Checks if an image is upright, based on the coordinates of the QR code
        in the image.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.
            config (dict): A dictionary containing the config file values.

        Returns:
            bool: True if image is upright, False otherwise.

        """
        qr_code = self.decode_qr(page)
        qr_x = qr_code.rect.left
        qr_y = qr_code.rect.top
        x_error = config['x_error']
        y_error = config['y_error']

        if ((config['qr_x'] - x_error <= qr_x <= config['qr_x'] + x_error) and 
                (config['qr_y'] - y_error <= qr_y <= config['qr_y'] + y_error)):
            return True
        else:
            return False

    def upright_image(self, page, config):
        """
        Rotates an image by 90 degree increments until it is upright.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.
            config (dict): A dictionary containing the config file values.

        Returns:
            page (numpy.ndarray): An ndarray representing the upright test 
                image.

        """
        if self.image_is_upright(page, config):
            return page
        else:
            for _ in range(3):
                page = utils.rotate_image(page, 90)
                if self.image_is_upright(page, config):
                    return page
        return None

    def scale_config_r(self, config, x_scale, y_scale, re_x, re_y):
        """
        Recursively scales lists within lists of values in the config dictionary 
        based on the width and height of the image being graded.  

        Args:
            config (dict): An unscaled coordinate mapping read from the 
                configuration file.
            x_scale (int): Factor to scale x coordinates by.
            y_scale (int): Factor to scale y coordinates by.
            re_x (pattern): Regex pattern to match x coordinate key names.
            re_y (pattern): Regex pattern to match y coordinate key names.

        Returns:
            config (dict): A scaled coordinate mapping read from the 
                configuration file. 

        """
        for key, val in config.items():
            if isinstance(val, list):
                for config in val:
                    self.scale_config_r(config, x_scale, y_scale, re_x, re_y)
            if re_x.search(key) or key == 'bubble_width':
                config[key] = val * x_scale
            elif re_y.search(key) or key == 'bubble_height':
                config[key] = val * y_scale

    def scale_config(self, config, width, height):
        """
        Scales the values in the config dictionary based on the width and height
        of the image being graded.

        Args:
            config (dict): An unscaled coordinate mapping read from the 
                configuration file.
            width (int): Width of the actual test image.
            height (int): Height of the actual test image.

        """
        x_scale = width / config['page_width']
        y_scale = height / config['page_height']

        # Regex to match strings like x, qr_x, and x_min.
        re_x = re.compile('(_|^)x(_|$)')
        re_y = re.compile('(_|^)y(_|$)')
        
        self.scale_config_r(config, x_scale, y_scale, re_x, re_y)

    def grade(self, image_name, verbose_mode, debug_mode, scale):
        """
        Grades a test image and outputs the result to stdout as a JSON object.

        Args:
            image_name (str): Filepath to the test image to be graded.
            verbose_mode (bool): True to run program in verbose mode, False 
                otherwise.
            debug_mode (bool): True to run program in debug mode, False 
                otherwise.
            scale (str): Factor to scale image slices by.

        """
        # Initialize dictionary to be returned.
        data = {
            'status' : 0,
            'error' : ''
        }

        # Cast str to float for scale.
        if scale is None:
            scale = 1.0
        else:
            try:
                scale = float(scale)
            except ValueError:
                data['status'] = 1
                data['error'] = f'Scale {scale} must be of type float'
                return json.dump(data, sys.stdout)

        # Verify that scale is positive.
        if scale <= 0:
            data['status'] = 1
            data['error'] = f'Scale {scale} must be positive'
            return json.dump(data, sys.stdout)

        # Verify that the filepath leads to a .png
        if not (image_name.endswith('.png')):
            data['status'] = 1
            data['error'] = f'File {image_name} must be of type .png'
            return json.dump(data, sys.stdout)

        # Load image. 
        im = cv.imread(image_name)
        if im is None:
            data['status'] = 1
            data['error'] = f'Image {image_name} not found'
            return json.dump(data, sys.stdout);

        # Find test page within image.
        page = self.find_page(im)
        if page is None:
            data['status'] = 1
            data['error'] = f'Page not found in {image_name}'
            return json.dump(data, sys.stdout);   

        # Decode QR code, which will contain path to configuration file.
        qr_code = self.decode_qr(page)
        if qr_code is None:
            data['status'] = 1
            data['error'] = f'QR code not found in {image_name}'
            return json.dump(data, sys.stdout);
        else:
            config_fname = qr_code.data.decode('utf-8')
            config_fname = (os.path.dirname(os.path.abspath(sys.argv[0])) 
                + '/config/6q.json')

        # Read config file into dictionary and scale values. Check for duplicate
        # keys with object pairs hook.
        try:
            with open(config_fname) as file:
                config = json.load(file, 
                    object_pairs_hook=config_parser.duplicate_key_check)
        except FileNotFoundError:
            data['status'] = 1
            data['error'] = f'Configuration file {qrData} not found'
            return json.dump(data, sys.stdout)

        # Parse config file.
        parser = config_parser.Parser(config, config_fname)
        status, error = parser.parse()
        if status == 1:
            data['status'] = 1
            data['error'] = error
            return json.dump(data, sys.stdout)

        # Scale config values based on page size.
        self.scale_config(config, page.shape[1], page.shape[0])  

        # Rotate page until upright.
        page = self.upright_image(page, config)
        if page is None:
            data['status'] = 1
            data['error'] = f'Could not upright page in {image_name}'
            return json.dump(data, sys.stdout);

        # Grade each test box and add result to data.
        for box_config in config['boxes']:
            box_config['x_error'] = config['x_error']
            box_config['y_error'] = config['y_error']
            box_config['bubble_width'] = config['bubble_width']
            box_config['bubble_height'] = config['bubble_height']
            box = TestBox(page, box_config, verbose_mode, debug_mode, scale)
            data[box.name] = box.grade()

        # Output result as a JSON object to stdout.
        json.dump(data, sys.stdout)
        print()

        # For debugging.
        return json.dumps(data)


def main():
    """
    Parses command line arguments and grades the specified test.

    """
    # Parse the arguments.
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, 
        help='path to the input image')
    ap.add_argument('-v', action='store_true', required=False, 
        help='enable verbose mode')
    ap.add_argument('-d', action='store_true', required=False, 
        help='enable debug mode')
    ap.add_argument('-s', '--scale', required=False, help='scale image slices')
    args = vars(ap.parse_args())

    # Grade test.
    grader = Grader()
    return grader.grade(args['image'], args['v'], args['d'], args['scale'])


if __name__ == '__main__':
    main()
