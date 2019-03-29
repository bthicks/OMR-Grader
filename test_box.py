import cv2 as cv
from imutils import contours as cutils

import utils

class TestBox:

    def __init__(self, page, config, verbose_mode, debug_mode):
        '''
        Constructor for a new test box.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.
            config (dict): A dictionary containing the config file values for 
                this test box.
            verbose_mode (bool): True to run program in verbose mode, False 
                otherwise.
            debug_mode (bool): True to run the program in debug mode, False 
                otherwise.

        Returns:
            TestBox: A newly created test box.

        '''
        # Args.
        self.page = page
        self.config = config
        self.verbose_mode = verbose_mode
        self.debug_mode = debug_mode

        # Configuration values.
        self.name = config['name']
        self.type = config['type']
        self.orientation = config['orientation']
        self.x = config['x']
        self.y = config['y']
        self.rows = config['rows']
        self.columns = config['columns']
        self.groups = config['groups']
        self.bubble_width = config['bubble_width']
        self.bubble_height = config['bubble_height']
        self.x_error = config['x_error']
        self.y_error = config['y_error']

        # Return values.
        self.bubbled = []
        self.unsure = []
        self.images = []
        self.status = 0
        self.error = ''

    def is_bubble(self, contour, bubbles):
        '''
        Checks if a contour is of sufficient width and height, is somewhat
        circular, and is within the correct coordinates, with margins for error,
        to be counted as a bubble.

        Args:
            contour (numpy.ndarray): An ndarray representing the contour being 
                checked.
            bubbles (list): A list of lists, where each list is a group of
                bubble contours.

        '''
        (x, y, w, h) = cv.boundingRect(contour)
        aspect_ratio = w / float(h)

        # Add offsets to get coordinates in relation to the whole test image 
        # instead of in relation to the test box.
        x += self.x
        y += self.y

        # Ignore contour if not of sufficient width or height, or not circular.
        if (w < self.bubble_width * 0.9 or 
            h < self.bubble_height * 0.9 or
            aspect_ratio < 0.7 or
            aspect_ratio > 1.3):
            return

        # If the contour fits the coordinates of a bubble group, add it to that
        # group.
        for (i, group) in enumerate(self.groups):
            if (x >= group['x_min'] - self.x_error and
                x <= group['x_max'] + self.x_error and
                y >= group['y_min'] - self.y_error and
                y <= group['y_max'] + self.y_error):
                bubbles[i].append(contour)
                break

    def get_bubbles(self, box):
        '''
        Finds and return bubbles within the test box.

        Args:
            box (numpy.ndarray): An ndarray representing a test box.

        Returns:
            bubbles (list): A list of lists, where each list is a group of 
                bubble contours.

        '''
        # Find bubbles in box.
        _, contours, _ = cv.findContours(box, cv.RETR_EXTERNAL, 
            cv.CHAIN_APPROX_SIMPLE)

        # Init empty list for each group of bubbles.
        bubbles = []
        for i in range(len(self.groups)):
            bubbles.append([])

        # Check if contour is bubble; if it is, add to its appropriate group.
        for contour in contours:
            self.is_bubble(contour, bubbles)

        return bubbles

    def is_box(self, contour):
        '''
        Checks if x and y coordinates of a contour match the x and y coordinates
        of this test box, with margins for error.

        Args:
            contour (numpy.ndarray): An ndarray representing the contour being 
                checked.

        Returns:
            bool: True for success, False otherwise.

        '''
        (x, y, _, _) = cv.boundingRect(contour)

        if ((self.x - self.x_error <= x <= self.x + self.x_error) and 
            (self.y - self.y_error <= y <= self.y + self.y_error)):
            return True
        else:
            return False

    def get_box_helper(self, im):
        '''
        Finds and returns the box with bubbles as external contours, not a box
        within a box.

        Args:
            im (numpy.ndarray): An ndarray representing the possible test box.

        Returns:
            box (numpy.ndarray): An ndarray representing the test box.

        '''
        # Find external contours of the test box.
        _, contours, _ = cv.findContours(im, cv.RETR_EXTERNAL, 
            cv.CHAIN_APPROX_SIMPLE)
        box = im

        # A box within a box will have 1 external contour; continue looping
        # until multiple external contours are found.
        while (len(contours) == 1):
            box = utils.get_transform(contours[0], im)
            _, contours, _ = cv.findContours(box, cv.RETR_EXTERNAL, 
                cv.CHAIN_APPROX_SIMPLE)

        return box

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
                box = utils.get_transform(contour, threshold)

                # Find inner contours to verify that the box contains bubbles.
                _, inner_contours, _ = cv.findContours(box, cv.RETR_TREE, 
                    cv.CHAIN_APPROX_SIMPLE)

                if (len(inner_contours) > 4):
                    return self.get_box_helper(box)

        return None

    def sort_bubbles(self, bubbles):
        '''
        Sorts a list of bubbles based on the test box orientation.

        Args:
            bubbles (list): A list of bubble contours.

        Returns:
            bubbles (list): A list of sorted bubble contours.

        '''
        if (self.orientation == "left-to-right"):
            bubbles, _ = cutils.sort_contours(bubbles, method="top-to-bottom")
        elif (self.orientation == "top-to-bottom"):
            bubbles, _ = cutils.sort_contours(bubbles, method="left-to-right")

        return bubbles

    def grade_bubbles(self, bubbles):
        '''
        Grades a list of bubbles from the test box.

        Args:
            bubbles (list): A list of lists, where each list is a group of 
                bubble contours.

        '''
        for group in bubbles:
            group = self.sort_bubbles(group)

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

        # Find box, find bubbles in box, then grade bubbles.
        box = self.get_box()
        bubbles = self.get_bubbles(box)
        self.grade_bubbles(bubbles)

        # Add results of grading to return value.
        data['bubbled'] = self.bubbled
        data['unsure'] = self.unsure
        data['images'] = self.images
        data['status'] = self.status
        data['error'] = self.error

        return data

