from imutils.perspective import four_point_transform
from imutils import contours as cutils
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

   # check if answer contour is within the correct coordinates
   def answerInBounds(self, x, y):
      if 25 <= y <= 100:
         if 160 <= x <= 490:
            return True
         elif 930 <= x <= 1250:
            return True
         elif 1690 <= x <= 2010:
            return True
      return False  

   # check if version contour is within the correct coordinates
   def versionInBounds(self, x, y):
      if 750 <= x <= 1080 and 310 <= y <= 320:
         return True
      else:
         return False

   # check if id contour is within the correct coordinates
   def idInBounds(self, x, y):
      if 15 <= x <= 760 and 10 <= y <= 600:
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
      # threshold the page and find boxes within the page
      _, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
      _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      contours = sorted(contours, key=cv.contourArea, reverse=True)

      (_, self.answersOffset, _, _) = cv.boundingRect(contours[6])
      peri = cv.arcLength(contours[6], True)
      approx = cv.approxPolyDP(contours[6], 0.02 * peri, True)
      return four_point_transform(threshold, approx.reshape(4, 2))

   # return contour for version box in test
   def getVersionContour(self):
         # threshold the page and find boxes within the page
      _, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
      _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      contours = sorted(contours, key=cv.contourArea, reverse=True)

      peri = cv.arcLength(contours[4], True)
      approx = cv.approxPolyDP(contours[4], 0.02 * peri, True)
      return four_point_transform(threshold, approx.reshape(4, 2))

   # return contour for id contour in test
   def getIdContour(self):
      # threshold the page and find boxes within the page
      _, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
      _, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      contours = sorted(contours, key=cv.contourArea, reverse=True)

      peri = cv.arcLength(contours[3], True)
      approx = cv.approxPolyDP(contours[3], 0.02 * peri, True)
      return four_point_transform(threshold, approx.reshape(4, 2))

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

            # if ~50% bubbled, count as marked
            if total > 1600:
               bubbled += chr(j + 65)
            # count as unsure 
            elif total > 1000:
               bubbled = '?'
               self.unsure.append(question + 1 + (2 * columnNum))
               self.images.append(self.getImageSlice(question + 1 + (2 * columnNum), minY, maxY, self.answersOffset))
               break

         self.answers.append(bubbled)

   def gradeAnswers(self, answersContour):
      # find bubbles in question box
      _, allContours, _ = cv.findContours(answersContour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      answerContours = []
      yValues = []
      height = None

      for contour in allContours:
         (x, y, w, h) = cv.boundingRect(contour)

         if w >= 45 and h >= 45 and self.answerInBounds(x, y):
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

         if w >= 45 and h >= 45 and self.versionInBounds(x, y):
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
      _, allContours, _ = cv.findContours(idContour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
      idContours = []

      for contour in allContours:
         (x, y, w, h) = cv.boundingRect(contour)

         if w >= 45 and h >= 45 and self.idInBounds(x, y):
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
