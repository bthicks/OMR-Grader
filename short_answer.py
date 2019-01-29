from imutils.perspective import four_point_transform
from imutils import contours as cutils
import math
import numpy as np 
import cv2 as cv

class ShortAnswerTest:

    def __init__(self, page):
        self.page = page
        self.answers = []
        self.unsure = []
        self.images = []
        self.version = None
        self.id = ""
        self.answersOffset = None
        self.std_config = {'page_width': 565.06, 'page_height': 259, 
            'bubble_width': 10.8, 'bubble_height': 10.8, 'qr_x': 23.79, 'qr_y': 136.88,
            'id_rows': 10, 'id_columns': 9, 'id_x': 343.03, 'id_y': 34.89, 
            'id_x_min': 348.53, 'id_x_max': 524.46, 'id_y_min': 39.43, 
            'id_y_max': 177.54, 'version_x': 23.65, 'version_y': 20.86, 
            'version_x_min': 208.25, 'version_x_max': 293.17, 'version_y_min': 96.12, 
            'version_y_max': 106.92, 'answer_x': 23.65, 'answer_y': 202.63, 
            'answer_x_min_1': 65.07, 'answer_x_max_1': 139.19, 'answer_x_min_2': 248.45,
            'answer_x_max_2': 322.58, 'answer_x_min_3': 432.05, 'answer_x_max_3': 506.17,
            'answer_y_min': 210.44, 'answer_y_max': 227.14, 'x_error': 8.1, 'y_error': 8.1}
        self.x_scale = self.page.shape[1] / self.std_config['page_width']
        self.y_scale = self.page.shape[0] / self.std_config['page_height']
        self.config = {}
        for key, val in self.std_config.items():
            if 'x' in key or key == 'bubble_width':
                self.config[key] = val * self.x_scale
            elif 'y' in key or key == 'bubble_height':
                self.config[key] = val * self.y_scale
            else:
                self.config[key] = val

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

            if (self.config['answer_x'] - 10 <= x <= self.config['answer_x'] + 10 
                    and self.config['answer_y'] - 10 <= y <= self.config['answer_y'] + 10):
                (_, self.answersOffset, _, _) = cv.boundingRect(contour)            
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        print("Answers contour not found")
        exit(0)

    # return contour for version box in test
    def getVersionContour(self):
        # blur then threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.config['version_x'] - 10 <= x <= self.config['version_x'] + 10 
                    and self.config['version_y'] - 10 <= y <= self.config['version_y'] + 10):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        print("Version contour not found")
        exit(0)

    # return contour for id contour in test
    def getIdContour(self):
        # threshold the page and find boxes within the page
        blurred = cv.GaussianBlur(self.page, (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            (x, y, _, _) = cv.boundingRect(contour)

            if (self.config['id_x'] - 10 <= x <= self.config['id_x'] + 10 
                    and self.config['id_y'] - 10 <= y <= self.config['id_y'] + 10):
                peri = cv.arcLength(contour, True)
                approx = cv.approxPolyDP(contour, 0.02 * peri, True)
                return four_point_transform(threshold, approx.reshape(4, 2))

        print("Version contour not found")
        exit(0)

    def gradeAnswersColumn(self, column, columnNum, answersContour, minY, maxY):
        # each field has 5 bubbles so loop in batches of 5
        for (question, i) in enumerate(np.arange(0, len(column), 5)):
            contours, _ = cutils.sort_contours(column[i:i + 5])
            bubble_area = math.pi * (self.config['bubble_width'] / 2) ** 2
            #print('area:', bubble_area)
            bubbled = ""

            for (j, c) in enumerate(contours):
                mask = np.zeros(answersContour.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(answersContour, answersContour, mask=mask)
                total = cv.countNonZero(mask)
                area = cv.contourArea(c)

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
 
            if (w >= self.config['bubble_width']  
                    and h >= self.config['bubble_height']  
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

            if (w >= self.config['bubble_width'] 
                    and h >= self.config['bubble_height'] 
                    and self.versionInBounds(x, y)):
                versionContours.append(contour)

        # grade bubbles in version box
        versionContours, _ = cutils.sort_contours(versionContours, method="left-to-right")
        maxCount = None

        for (j, c) in enumerate(versionContours):
            mask = np.zeros(versionContour.shape, dtype="uint8")
            cv.drawContours(mask, [c], -1, 255, -1)
            mask = cv.bitwise_and(versionContour, versionContour, mask=mask)
            total = cv.countNonZero(mask)

            if self.version is None or total > maxCount:
                self.version = chr(j + 65)
                maxCount = total

    def gradeId(self, idContour):
        # find bubbles in id box
        _, allContours, _ = cv.findContours(idContour, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        idContours = []

        for contour in allContours:
            (x, y, w, h) = cv.boundingRect(contour)
            x += self.config['id_x']
            y += self.config['id_y']

            if (w >= self.config['bubble_width'] 
                    and h >= self.config['bubble_height'] 
                    and self.idInBounds(x, y)):
                idContours.append(contour)

        # grade bubbles in id box
        idContours, _ = cutils.sort_contours(idContours, method="left-to-right")

        # each field has 10 possibilities so loop in batches of 10
        for (q, i) in enumerate(np.arange(0, len(idContours), 10)):
            contours, _ = cutils.sort_contours(idContours[i:i + 10], method="top-to-bottom")
            bubbled = None
            maxCount = None

            for (j, c) in enumerate(contours):
                mask = np.zeros(idContour.shape, dtype="uint8")
                cv.drawContours(mask, [c], -1, 255, -1)
                mask = cv.bitwise_and(idContour, idContour, mask=mask)
                total = cv.countNonZero(mask)

                if bubbled is None or total > maxCount:
                    bubbled = j
                    maxCount = total

            self.id += str(bubbled)
