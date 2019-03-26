import cv2 as cv

import utils

class TestBox:

    def __init__(self, page, config, verbose_mode, debug_mode):
        '''
        Constructor for a new test box.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.
            config (dict): A dictionary containing the config file values for this
                test box.
            verbose_mode (bool): True to run program in verbose mode, False 
                otherwise.
            debug_mode (bool): True to run the program in debug mode, False 
                otherwise.

        Returns:
            TestBox: A newly created test box.

        '''
        self.page = page
        self.config = config
        self.verbose_mode = verbose_mode
        self.debug_mode = debug_mode

        self.name = config['name']
        self.type = config['type']
        self.orientation = config['orientation']
        self.x = config['x']
        self.y = config['y']
        self.rows = config['rows']
        self.columns = config['columns']
        self.groups = config['groups']
        self.x_error = config['x_error']
        self.y_error = config['y_error']

        self.bubbled = []
        self.unsure = []
        self.images = []
        self.status = 0

    def is_box(self, contour):
        """
        Checks if x and y coordinates of a contour match the x and y coordinates
        of this test box, with margins for error.

        Args:
            contour (numpy.ndarray): An ndarray representing the contour being 
                checked.

        Returns:
            bool: True for success, False otherwise.

        """
        (x, y, _, _) = cv.boundingRect(contour)

        if ((self.x - self.x_error <= x <= self.x + self.x_error) 
            and (self.y - self.y_error <= y <= self.y + self.y_error)):
            return True
        else:
            return False

    def get_box(self):
        '''
        Finds and returns the contour for this test answer box.

        Returns:
            numpy.ndarray: An ndarray representing the answer box in
                the test image.

        '''
        # Blur and threshold the page, then find boxes within the page.
        threshold = utils.get_threshold(self.page)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, 
            cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        # Iterate through contours until the correct box is found.
        for contour in contours:
            if (self.is_box(contour)):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    def grade(self):
        '''
        Finds and grades a test box within a test image.

        Returns:
            data (dict): A dictionary containing info about the graded test box.

        '''
        # Initialize dictionary to be returned.
        data = {
            'status' : 0,
            'error' : ''
        }

        return data

