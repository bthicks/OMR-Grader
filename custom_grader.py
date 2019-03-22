import os
import sys
import argparse
import base64
import json
import math
import re

import cv2 as cv
from imutils.perspective import four_point_transform
import pyzbar.pyzbar as pyzbar
import numpy as np 

import custom_test


class CustomGrader:

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
        return

    def image_is_upright(self, page):
        """
        Checks if an image is upright, based on the coordinates of the QR code
        in the image

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            bool: True if image is upright, False otherwise.

        """
        return

    def upright_image(self, page):
        """
        Rotates an image by 90 degree increments until it is upright.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.

        Returns:
            page (numpy.ndarray): An ndarray representing the upright test 
                image.

        """
        return


    def scale_config_r(self, config, x_scale, y_scale, re_x, re_y):
        """
        Recursively scales lists within lists of values in the config dictionary 
        based on the width and height of the image being graded.  

        Args:
            config (dict): An unscaled coordinate mapping read from the 
                configuration file.
            x_scale (int): Factor to scale x coordinates by.
            y_scale (int): Factor to scale y coordinates by.
            re_x (pattern): Regex pattern to match x coordinate key names
            re_y (pattern): Regex pattern to match y coordinate key names

        Returns:
            config (dict): A scaled coordinate mapping read from the 
                configuration file. 

        """
        for key, val in config.items():
            if isinstance(val, list):
                for config in val:
                    self.scale_config_r(config, x_scale, y_scale, re_x, re_y)
            if (re_x.search(key) or key == 'bubble_width'):
                config[key] = val * x_scale
            elif (re_y.search(key) or key == 'bubble_height'):
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

        # Regex to match strings like x, qr_x, and x_min
        re_x = re.compile('(_|^)x(_|$)')
        re_y = re.compile('(_|^)y(_|$)')
        
        self.scale_config_r(config, x_scale, y_scale, re_x, re_y)

    def encode_image(self, image):
        """
        Encodes a .png image into a base64 string.

        Args:
            image (numpy.ndarray): An ndarray representing an image.

        Returns:
            str: A base64 string encoding of the image.

        """
        return

    def grade(self, image_name, verbose_mode, debug_mode):
        """
        Grades a test image and outputs the result to stdout as a JSON object.

        Args:
            image_name (str): Filepath to the test image to be graded.

        """
        # Set window size for displayed images when debugging
        if (debug_mode):
            cv.namedWindow(image_name, cv.WINDOW_NORMAL)
            cv.resizeWindow(image_name, 850, 1100)

        #Initialize dictionary to be returned
        data = {
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
            config_fname = qr_code.data.decode('utf-8')
            config_fname = (os.path.dirname(os.path.abspath(sys.argv[0])) 
                + '/config/custom_6q.json')     

        # Read config file into dictionary and scale values.
        try:
            with open(config_fname) as file:
                config = json.load(file)
            self.scale_config(config, page.shape[1], page.shape[0])
        except FileNotFoundError:
            data['status'] = 1
            data['error'] = 'Configuration file', qrData, 'not found'
            return json.dump(data, sys.stdout);     

        

        # Output result as a JSON object to stdout
        json.dump(data, sys.stdout)

        # For debugging
        return json.dumps(data)


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
    grader = CustomGrader()
    return grader.grade(args['image'], args['v'], args['d'])

if (__name__ == '__main__'):
    main()
