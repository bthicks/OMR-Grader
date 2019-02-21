import math

import cv2 as cv
import numpy as np 
from imutils import contours as cutils
from imutils.perspective import four_point_transform


class ShortAnswerTest:

    def __init__(self, page, config):
        """
        Constructor for a short answer test.

        Args:
            page (numpy.ndarray): An ndarray representing the test image.
            config (dict): Coordinate mapping read from the configuation file.

        """
        self.page = page
        self.answers = []
        self.unsure = []
        self.images = []
        self.version = None
        self.id = ""
        self.answers_offset = None
        self.config = config

    def get_answers(self):
        """
        Getter for the test answers.

        Returns:
            answers (list): A list of graded answers.

        """
        return self.answers

    def get_unsure(self):
        """
        Getter for the unsure test question numbers.

        Returns:
            answers (list): A list of unsure answer numbers.

        """
        return self.unsure

    def get_images(self):
        """
        Getter for the unsure test question image slices.

        Returns:
            images (list): A list of test question image slices.

        """
        return self.images

    def get_version(self):
        """
        Getter for the test version.

        Returns:
            version (str): The test version.

        """
        return self.version

    def get_id(self):
        """
        Getter for the student id number.

        Returns:
            id (str): The student id number.

        """
        return self.id

    def is_answer_bubble(self, x, y, w, h):
        """
        Checks if an answer bubble is of sufficient width and height, somewhat 
        circular, and if its x and y coordinates are within the correct 
        coordinates, with margins for error.

        Args:
            x (int): X coordinate of bubble being checked.
            y (int): Y coordinate of bubble being checked.
            w (int): Width of bubble being checked.
            h (int): Height of bubble being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (w >= self.config['bubble_width'] * 0.9 and
            h >= self.config['bubble_height'] * 0.9 and
            0.7 <= w / float(h) <= 1.3 and
            y >= self.config['answer_y_min'] - self.config['y_error'] and
            y <= self.config['answer_y_max'] + self.config['y_error']):
            if (x >= self.config['answer_x_min_1'] - self.config['x_error'] and
                x <= self.config['answer_x_max_1'] + self.config['x_error']):
                return True
            elif (x >= self.config['answer_x_min_2'] - self.config['x_error'] and
                  x <= self.config['answer_x_max_2'] + self.config['x_error']):
                return True
            elif (x >= self.config['answer_x_min_3'] - self.config['x_error'] and
                  x <= self.config['answer_x_max_3'] + self.config['x_error']):
                return True
        return False 

    def is_answer_box(self, x, y):
        """
        Checks if x and y coordinates of a contour match the x and y
        coordinates of the answer box, with margins for error.

        Args:
            x (int): X coordinate of contour being checked.
            y (int): Y coordinate of contour being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (x >= self.config['answer_x'] - self.config['x_error'] and  
            x <= self.config['answer_x'] + self.config['x_error'] and
            y >= self.config['answer_y'] - self.config['y_error'] and 
            y <= self.config['answer_y'] + self.config['y_error']):
            return True
        else:
            return False 

    def is_version_bubble(self, x, y, w, h):
        """
        Checks if a version bubble is of sufficient width and height, somewhat 
        circular, and if its x and y coordinates are within the correct 
        coordinates, with margins for error.

        Args:
            x (int): X coordinate of bubble being checked.
            y (int): Y coordinate of bubble being checked.
            w (int): Width of bubble being checked.
            h (int): Height of bubble being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (w >= self.config['bubble_width'] * 0.9 and
            h >= self.config['bubble_height'] * 0.9 and
            0.7 <= w / float(h) <= 1.3 and
            x >= self.config['version_x_min'] - self.config['x_error'] and 
            x <= self.config['version_x_max'] + self.config['x_error'] and 
            y >= self.config['version_y_min'] - self.config['y_error'] and 
            y <= self.config['version_y_max'] + self.config['y_error']):
            return True
        else:
            return False

    def is_version_box(self, x, y):
        """
        Checks if x and y coordinates of a contour match the x and y
        coordinates of the version box, with margins for error.

        Args:
            x (int): X coordinate of contour being checked.
            y (int): Y coordinate of contour being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (x >= self.config['version_x'] - self.config['x_error'] and  
            x <= self.config['version_x'] + self.config['x_error'] and
            y >= self.config['version_y'] - self.config['y_error'] and 
            y <= self.config['version_y'] + self.config['y_error']):
            return True
        else:
            return False

    def is_id_bubble(self, x, y, w, h):
        """
        Checks if an id bubble is of sufficient width and height, somewhat 
        circular, and if its x and y coordinates are within the correct 
        coordinates, with margins for error.

        Args:
            x (int): X coordinate of bubble being checked.
            y (int): Y coordinate of bubble being checked.
            w (int): Width of bubble being checked.
            h (int): Height of bubble being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (w >= self.config['bubble_width'] * 0.9 and
            h >= self.config['bubble_height'] * 0.9 and
            0.7 <= w / float(h) <= 1.3 and
            x >= self.config['id_x_min'] - self.config['x_error'] and 
            x <= self.config['id_x_max'] + self.config['x_error'] and
            y >= self.config['id_y_min'] - self.config['y_error'] and 
            y <= self.config['id_y_max'] + self.config['y_error']):
            return True
        else:
            return False

    def is_id_box(self, x, y):
        """
        Checks if x and y coordinates of a contour match the x and y
        coordinates of the id box, with margins for error.

        Args:
            x (int): X coordinate of contour being checked.
            y (int): Y coordinate of contour being checked.

        Returns:
            bool: True for success, False otherwise.

        """
        if (x >= self.config['id_x'] - self.config['x_error'] and  
            x <= self.config['id_x'] + self.config['x_error'] and
            y >= self.config['id_y'] - self.config['y_error'] and 
            y <= self.config['id_y'] + self.config['y_error']):
            return True
        else:
            return False

    def get_image_slice(self, x_min, x_max, y_min, y_max):
        """
        Crops and returns image slice for undetermined questions.

        Args:
            x_min (float): Minimum x coordinate.
            x_max (float): Maximum x coordinate.
            y_min (float): Minimum y coordinate.
            y_max (float): Maximum y coordinate.

        Returns:
            numpy.ndarray: An ndarray representing the specified question in the
                test image.

        """
        # Stretched x and y bounaries, by somewhat arbitrary numbers, to 
        # encompass entire question.
        x_min -= self.config['x_error']
        x_max += (self.config['bubble_width'] + self.config['x_error'])
        y_max += (self.config['bubble_height'] * 1.2)

        return self.page[int(y_min) : int(y_max), int(x_min) : int(x_max)]

    def get_answer_box(self):
        """
        Finds and returns the contour for the test answer box.

        Returns:
            answers (numpy.ndarray): An ndarray representing the answer box in
                the test image.

        """
        # Blur then threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        # Iterate through contours until the answer box is found.
        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.is_answer_box(x, y)):
                (_, self.answers_offset, _, _) = cv.boundingRect(contour)            
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                contour = four_point_transform(threshold, approx.reshape(4, 2))

                # Find inner contours and verify that the answer box contains
                # answers bubbles.
                _, inner_contours, _ = cv.findContours(contour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

                if (len(inner_contours) > 4):
                    return contour

        return None

    def get_version_box(self):
        """
        Finds and returns the contour for the test version box.

        Returns:
            answers (numpy.ndarray): An ndarray representing the version box in
                the test image.

        """
        # Blur then threshold the page and find boxes within the page.
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        # Iterate through contours until the version box is found.
        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.is_version_box(x, y)):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    def get_id_box(self):
        """
        Finds and returns the contour for the test id box.

        Returns:
            answers (numpy.ndarray): An ndarray representing the id box in the
                test image.

        """
        # Blur then threshold the page and find boxes within the page.
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        # Iterate through contours until the id box is found.
        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.is_id_box(x, y)):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    def get_answer_bubbles(self, answer_box):
        """
        Finds and return bubbles within the answer box.

        Args:
            answer_box (numpy.ndarray): An ndarray representing the answer box 
                in the test image.

        Returns:
            list: A list of contours for each bubble in the answer box.

        """
        # Find bubbles in question box.
        _, contours, _ = cv.findContours(answer_box, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        bubbles = []
        yValues = []
        height = None

        # Verify that bubbles are counted as external contours (instead of a
        # box within the answer box). 
        while (len(contours) == 1):
            peri = cv.arcLength(contours[0], True)
            approx = cv.approxPolyDP(contours[0], 0.02 * peri, True)
            contours = four_point_transform(answer_box, approx.reshape(4, 2))
            _, contours, _ = cv.findContours(contours, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['answer_x']
            y += self.config['answer_y']

            if (self.is_answer_bubble(x, y, w, h)):
                bubbles.append(contour)
                yValues.append(y)
                height = h

        return bubbles

    def grade_answer_column(self, column, column_num, answer_box):
        """
        Helper function to grade a single column of bubbles within the answer box.

        Args:
            column (tuple): A list of bubbles for an answer column.
            answer_box (numpy.ndarray): An ndarray representing the answer box 
                in the test image.

        """
        # Each field has 5 bubbles so loop in batches of 5.
        for (question, i) in enumerate(np.arange(0, len(column), 5)):
            contours, _ = cutils.sort_contours(column[i:i + 5])
            bubbled = ""
            bounding_rects = []

            # Calculate x and y boundaries of this question for image slicing.
            for (j, c) in enumerate(contours):
                bounding_rects.append(cv.boundingRect(c))

            x_min = min(bounding_rects, key=lambda x: x[0])[0] + self.config['answer_x']
            x_max = max(bounding_rects, key=lambda x: x[0])[0] + self.config['answer_x']
            y_min = min(bounding_rects, key=lambda x: x[1])[1] + self.config['answer_y']
            y_max = max(bounding_rects, key=lambda x: x[1])[1] + self.config['answer_y']

            # For each bubble in this question.
            for (j, c) in enumerate(contours):
                mask = np.zeros(answer_box.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(answer_box, answer_box, mask=mask)
                total = cv.countNonZero(mask)
                (x, y, w, h) = cv.boundingRect(c)
                area = math.pi * ((min(w, h) / 2) ** 2)

                # If ~50% bubbled, count as marked.
                if (total / area) > 0.8:
                    bubbled += chr(j + 65)
                # Count as unsure. 
                elif (total / area) > 0.75:
                    bubbled = '?'
                    self.unsure.append(question + 1 + (2 * column_num))
                    self.images.append(self.get_image_slice(x_min, x_max, y_min, y_max))
                    break

            self.answers.append(bubbled)

    def grade_answers(self, answer_box):
        """
        Finds and grades bubbles within the answer box.

        Args:
            answer_box (numpy.ndarray): An ndarray representing the answer box 
                in the test image.

        """
        # Get and grade bubbles in question box.
        bubbles = self.get_answer_bubbles(answer_box)
        bubbles, _ = cutils.sort_contours(bubbles, method="left-to-right")
        third = int(len(bubbles) / 3)
        column_1 = bubbles[0 : third]
        column_2 = bubbles[third : 2 * third]
        column_3 = bubbles[2 * third : 3 * third]

        # Grade questions 1-2.
        column_1, _ = cutils.sort_contours(column_1, method="top-to-bottom")
        self.grade_answer_column(column_1, 0, answer_box)

        # Grade questions 3-4.
        column_2, _ = cutils.sort_contours(column_2, method="top-to-bottom")
        self.grade_answer_column(column_2, 1, answer_box)

        # Grade questions 5-6.
        column_3, _ = cutils.sort_contours(column_3, method="top-to-bottom")
        self.grade_answer_column(column_3, 2, answer_box)

    def get_version_bubbles(self, version_box):
        """
        Finds and return bubbles within the version box.

        Args:
            version_box (numpy.ndarray): An ndarray representing the version box 
                in the test image.

        Returns:
            list: A list of contours for each bubble in the version box.

        """
        # Find bubbles in version box.
        _, contours, _ = cv.findContours(version_box, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        bubbles = []

        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['version_x']
            y += self.config['version_y']

            if (self.is_version_bubble(x, y, w, h)):
                bubbles.append(contour)

        return bubbles

    def grade_version(self, version_box):
        """
        Finds and grades bubbles within the version box.

        Args:
            version_box (numpy.ndarray): An ndarray representing the version box
                in the test image.

        """
        # Get and grade bubbles in version box.
        bubbles = self.get_version_bubbles(version_box)
        bubbles, _ = cutils.sort_contours(bubbles, method="left-to-right")
        bubbled = ""

        for (j, c) in enumerate(bubbles):
            mask = np.zeros(version_box.shape, dtype="uint8")
            cv.drawContours(mask, [c], -1, 255, -1)
            mask = cv.bitwise_and(version_box, version_box, mask=mask)
            total = cv.countNonZero(mask)
            (x, y, w, h) = cv.boundingRect(c)
            area = math.pi * ((min(w, h) / 2) ** 2)

            # If ~50% bubbled, count as marked.
            if (total / area) > 0.8:
                bubbled += chr(j + 65)
            # Count as unsure.
            elif (total / area > 0.75):
                bubbled = '?'
                break;

        self.version = bubbled

    def get_id_bubbles(self, id_box):
        """
        Finds and return bubbles within the student id box.

        Args:
            id_box (numpy.ndarray): An ndarray representing the id box in the 
                test image.

        Returns:
            list: A list of contours for each bubble in the student id box.

        """
        # Find bubbles in id box.
        _, contours, _ = cv.findContours(id_box, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        bubbles = []

        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['id_x']
            y += self.config['id_y']

            if (self.is_id_bubble(x, y, w, h)):
                bubbles.append(contour)

        return bubbles

    def grade_id(self, id_box):
        """
        Finds and grades bubbles within the student id box.

        Args:
            id_box (numpy.ndarray): An ndarray representing the id box in the 
                test image.

        """
        # Get and grade bubbles in id box.
        bubbles = self.get_id_bubbles(id_box)
        bubbles, _ = cutils.sort_contours(bubbles, method="left-to-right")

        # Each field has 10 possibilities so loop in batches of 10.
        for (q, i) in enumerate(np.arange(0, len(bubbles), 10)):
            contours, _ = cutils.sort_contours(bubbles[i:i + 10], method="top-to-bottom")
            bubbled = None
            max_count = -float("inf")

            for (j, c) in enumerate(contours):
                mask = np.zeros(id_box.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(id_box, id_box, mask=mask)
                total = cv.countNonZero(mask)
                (x, y, w, h) = cv.boundingRect(c)
                area = math.pi * ((min(w, h) / 2) ** 2)

                # If ~50% bubbled, count as marked.
                if (total / area) > 0.8 and total > max_count:
                    bubbled = j
                    max_count = total
                # Count as unsure.
                elif (total / area > 0.75):
                    bubbled = '?'
                    break;

            if bubbled is None:
                bubbled = '-'

            self.id += str(bubbled)

