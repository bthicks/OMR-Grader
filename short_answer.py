from imutils.perspective import four_point_transform
from imutils import contours as cutils
import math
import numpy as np 
import cv2 as cv

class ShortAnswerTest:

    def __init__(self, page, config):
        self.page = page
        self.answers = []
        self.unsure = []
        self.images = []
        self.version = None
        self.id = ""
        self.answersOffset = None
        self.config = config

    def getAnswers(self):
        return self.answers

    def getUnsure(self):
        return self.unsure

    def getImages(self):
        return self.images

    def getVersion(self):
        return self.version

    def getId(self):
        return self.id

    # check if answer bubble is within the correct coordinates
    def answerInBounds(self, x, y):
        if self.config['answer_y_min'] - self.config['y_error'] <= y <= self.config['answer_y_max'] + self.config['y_error']:
            if self.config['answer_x_min_1'] - self.config['x_error'] <= x <= self.config['answer_x_max_1'] + self.config['x_error']:
                return True
            elif self.config['answer_x_min_2'] - self.config['x_error'] <= x <= self.config['answer_x_max_2'] + self.config['x_error']:
                return True
            elif self.config['answer_x_min_3'] - self.config['x_error'] <= x <= self.config['answer_x_max_3'] + self.config['x_error']:
                return True
        return False  

    # check if version bubble is within the correct coordinates
    def versionInBounds(self, x, y):
        if (self.config['version_x_min'] - self.config['x_error'] <= x <= self.config['version_x_max'] + self.config['x_error'] 
                and self.config['version_y_min'] - self.config['y_error'] <= y <= self.config['version_y_max'] + self.config['y_error']):
            return True
        else:
            return False

    # check if id bubble is within the correct coordinates
    def idInBounds(self, x, y):
        if (self.config['id_x_min'] - self.config['x_error'] <= x <= self.config['id_x_max'] + self.config['x_error'] 
                and self.config['id_y_min'] - self.config['y_error'] <= y <= self.config['id_y_max'] + self.config['y_error']):
            return True
        else:
            return False

    # crop image slice for undetermined questions
    def getImageSlice(self, questionNum, minY, maxY, offset):
        diff = int((maxY - minY) / 2)

        if 1 <= questionNum <= 2:
            return self.page[(offset + minY + diff * (questionNum - 1)) : (offset + minY + diff * questionNum), 160 : 660]
        elif 3 <= questionNum <= 4:
            return self.page[(offset + minY + diff * (questionNum - 3)) : (offset + minY + diff * (questionNum - 2)), 930 : 1430]
        elif 5 <= questionNum <= 6:
            return self.page[(offset + minY + diff * (questionNum - 5)) : (offset + minY + diff * (questionNum - 4)), 1690 : 2190]
        else:
            return None

    # return contour for answers box in test
    def getAnswersContour(self):
        # blur then threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.config['answer_x'] - self.config['x_error'] <= x <= self.config['answer_x'] + self.config['x_error'] 
                    and self.config['answer_y'] - self.config['y_error'] <= y <= self.config['answer_y'] + self.config['y_error']):
                (_, self.answersOffset, _, _) = cv.boundingRect(contour)            
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    # return contour for version box in test
    def getVersionContour(self):
        # blur then threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.config['version_x'] - self.config['x_error'] <= x <= self.config['version_x'] + self.config['x_error']
                    and self.config['version_y'] - self.config['y_error'] <= y <= self.config['version_y'] + self.config['y_error']):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    # return contour for id contour in test
    def getIdContour(self):
        # threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.config['id_x'] - self.config['x_error'] <= x <= self.config['id_x'] + self.config['x_error'] 
                    and self.config['id_y'] - self.config['y_error'] <= y <= self.config['id_y'] + self.config['y_error']):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        return None

    def gradeAnswersColumn(self, column, columnNum, answersContour, minY, maxY):
        # each field has 5 bubbles so loop in batches of 5
        for (question, i) in enumerate(np.arange(0, len(column), 5)):
            contours, _ = cutils.sort_contours(column[i:i + 5])
            bubbled = ""

            for (j, c) in enumerate(contours):
                mask = np.zeros(answersContour.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(answersContour, answersContour, mask=mask)
                total = cv.countNonZero(mask)
                (x, y, w, h) = cv.boundingRect(c)
                area = math.pi * ((min(w, h) / 2) ** 2)

                # if ~50% bubbled, count as marked
                if (total / area) > 0.8:
                    bubbled += chr(j + 65)
                # count as unsure 
                elif (total / area) > 0.7:
                    bubbled = '?'
                    #self.unsure.append(question + 1 + (2 * columnNum))
                    #self.images.append(self.getImageSlice(question + 1 + (2 * columnNum), minY, maxY, self.answersOffset))
                    break

            self.answers.append(bubbled)

    def gradeAnswers(self, answersContour):
        # find bubbles in question box
        _, allContours, _ = cv.findContours(answersContour, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        answerContours = []
        yValues = []
        height = None

        while (len(allContours) == 1):
            peri = cv.arcLength(allContours[0], True)
            approx = cv.approxPolyDP(allContours[0], 0.02 * peri, True)
            allContours = four_point_transform(answersContour, approx.reshape(4, 2)) 
            _, allContours, _ = cv.findContours(allContours, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in allContours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['answer_x']
            y += self.config['answer_y']
 
            if (w >= self.config['bubble_width'] * 0.9   
                    and h >= self.config['bubble_height'] * 0.9
                    and 0.7 <= w / float(h) <= 1.3
                    and self.answerInBounds(x, y)):
                answerContours.append(contour)
                yValues.append(y)
                height = h

        minY = yValues[len(yValues) - 1] - int(height * 0.1)
        maxY = yValues[0] + height + int(height * 0.25)

        # grade bubbles in question box
        answerContours, _ = cutils.sort_contours(answerContours, method="left-to-right")
        third = int(len(answerContours) / 3)
        column1 = answerContours[0 : third]
        column2 = answerContours[third : 2 * third]
        column3 = answerContours[2 * third : 3 * third]

        # grade questions 1-2
        column1, _ = cutils.sort_contours(column1, method="top-to-bottom")
        self.gradeAnswersColumn(column1, 0, answersContour, minY, maxY)

        # grade questions 3-4
        column2, _ = cutils.sort_contours(column2, method="top-to-bottom")
        self.gradeAnswersColumn(column2, 1, answersContour, minY, maxY)

        # grade questions 5-6
        column3, _ = cutils.sort_contours(column3, method="top-to-bottom")
        self.gradeAnswersColumn(column3, 2, answersContour, minY, maxY)

    def gradeVersion(self, versionContour):
        # find bubbles in version box
        _, allContours, _ = cv.findContours(versionContour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        versionContours = []

        for contour in allContours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['version_x']
            y += self.config['version_y']

            if (w >= self.config['bubble_width'] * 0.9
                    and h >= self.config['bubble_height'] * 0.9
                    and 0.7 <= w / float(h) <= 1.3
                    and self.versionInBounds(x, y))
                versionContours.append(contour)

        # grade bubbles in version box
        versionContours, _ = cutils.sort_contours(versionContours, method="left-to-right")
        bubbled = ""

        for (j, c) in enumerate(versionContours):
            mask = np.zeros(versionContour.shape, dtype="uint8")
            cv.drawContours(mask, [c], -1, 255, -1)
            mask = cv.bitwise_and(versionContour, versionContour, mask=mask)
            total = cv.countNonZero(mask)
            (x, y, w, h) = cv.boundingRect(c)
            area = math.pi * ((min(w, h) / 2) ** 2)

            # if ~50% bubbled, count as marked
            if (total / area) > 0.8:
                bubbled += chr(j + 65)
            # count as unsure
            elif (total / area > 0.7):
                bubbled = '?'
                break;

        self.version = bubbled

    def gradeId(self, idContour):
        # find bubbles in id box
        _, allContours, _ = cv.findContours(idContour, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        idContours = []

        for contour in allContours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['id_x']
            y += self.config['id_y']

            if (w >= self.config['bubble_width'] * 0.9
                    and h >= self.config['bubble_height'] * 0.9
                    and 0.7 <= w / float(h) <= 1.3
                    and self.idInBounds(x, y)):
                idContours.append(contour)

        # grade bubbles in id box
        idContours, _ = cutils.sort_contours(idContours, method="left-to-right")

        # each field has 10 possibilities so loop in batches of 10
        for (q, i) in enumerate(np.arange(0, len(idContours), 10)):
            contours, _ = cutils.sort_contours(idContours[i:i + 10], method="top-to-bottom")
            bubbled = None
            maxCount = -float("inf")

            for (j, c) in enumerate(contours):
                mask = np.zeros(idContour.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(idContour, idContour, mask=mask)
                total = cv.countNonZero(mask)
                (x, y, w, h) = cv.boundingRect(c)
                area = math.pi * ((min(w, h) / 2) ** 2)

                # if ~50% bubbled, count as marked
                if (total / area) > 0.8 and total > maxCount:
                    bubbled = j
                    maxCount = total
                # count as unsure
                elif (total / area > 0.7):
                    bubbled = '?'
                    break;

            if bubbled is None:
                bubbled = '-'

            self.id += str(bubbled)
