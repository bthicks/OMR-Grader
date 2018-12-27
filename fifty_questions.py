from imutils.perspective import four_point_transform
from imutils import contours as cutils
import numpy as np 
import cv2 as cv

class FiftyQuestionTest:

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
	@staticmethod
	def answerInBounds(x, y):
		if 70 <= y <= 1745:
			# within left column bounds
			if 180 <= x <= 500:
				return True
			# within right column bounds
			elif 705 <= x <= 1045:
				return True
			else:
				return False
		else:
			return False 

	# check if version contour is within the correct coordinates
	@staticmethod
	def versionInBounds(x, y):
		if 160 <= x <= 475 and 10 <= y <= 20:
			return True
		else:
			return False

	# check if id contour is within the correct coordinates
	@staticmethod
	def idInBounds(x, y):
		if 40 <= x <= 780 and 15 <= y <= 600:
			return True
		else:
			return False

  	# crop image slice for undetermined questions
	def getImageSlice(self, questionNum, minY, maxY, offset):
	
		diff = int((maxY - minY) / 25)

		if 1 <= questionNum <= 25:
			return self.page[(offset + minY + diff * (questionNum - 1)) : (offset + minY + diff * questionNum), 150 : 650]
		elif 26 <= questionNum <= 50:
			return self.page[(offset + minY + diff * (questionNum - 26)) : (offset + minY + diff * (questionNum - 25)), 675 : 1175]
		else:
			return None

	# return contour for answers box in test
	def getAnswersContour(self):
		# threshold the page and find boxes within the page
		_, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
		_, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		contours = sorted(contours, key=cv.contourArea, reverse=True)

		(_, self.answersOffset, _, _) = cv.boundingRect(contours[2])
		peri = cv.arcLength(contours[2], True)
		approx = cv.approxPolyDP(contours[2], 0.02 * peri, True)
		return four_point_transform(threshold, approx.reshape(4, 2))

	# return contour for version box in test
	def getVersionContour(self):
		# threshold the page and find boxes within the page
		_, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
		_, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		contours = sorted(contours, key=cv.contourArea, reverse=True)

		peri = cv.arcLength(contours[14], True)
		approx = cv.approxPolyDP(contours[14], 0.02 * peri, True)
		return four_point_transform(threshold, approx.reshape(4, 2))

	# return contour for id contour in test
	def getIdContour(self):
		# threshold the page and find boxes within the page
		_, threshold = cv.threshold(self.page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
		_, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		contours = sorted(contours, key=cv.contourArea, reverse=True)

		peri = cv.arcLength(contours[5], True)
		approx = cv.approxPolyDP(contours[5], 0.02 * peri, True)
		return four_point_transform(threshold, approx.reshape(4, 2))

	def gradeAnswers(self, answersContour):
		# find bubbles in question box
		_, allContours, _ = cv.findContours(answersContour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		answerContours = []
		yValues = []

		for contour in allContours:
			(x, y, w, h) = cv.boundingRect(contour)

			if w >= 45 and h >= 45 and self.answerInBounds(x, y):
				answerContours.append(contour)
				tup = (y, h)
				yValues.append(tup)

		minY = yValues[len(yValues) - 1][0]
		maxY = yValues[0][0] + yValues[0][1]

		# grade bubbles in question box
		answerContours, _ = cutils.sort_contours(answerContours, method="left-to-right")
		length = len(answerContours)
		mid = int(len(answerContours) / 2)
		column1 = answerContours[0 : mid]
		column2 = answerContours[mid : length]

		# grade questions 1-25
		column1, _ = cutils.sort_contours(column1, method="top-to-bottom")

		# each field has 5 bubbles so loop in batches of 5
		for (question, i) in enumerate(np.arange(0, len(column1), 5)):
			contours, _ = cutils.sort_contours(column1[i:i + 5])
			bubbled = ""

			for (j, c) in enumerate(contours):
				mask = np.zeros(answersContour.shape, dtype="uint8")
				cv.drawContours(mask, [c], -1, 255, -1)
				mask = cv.bitwise_and(answersContour, answersContour, mask=mask)
				total = cv.countNonZero(mask)

				# if ~50% bubbled, count as marked
				if total > 1700:
					bubbled += chr(j + 65)
				# count as unsure	
				elif total > 1000:
					bubbled = '?'
					self.unsure.append(question + 1)
					self.images.append(getImageSlice(question + 1, minY, maxY, self.answersOffset))
					break

			self.answers.append(bubbled)

		# grade questions 26-50
		column2, _ = cutils.sort_contours(column2, method="top-to-bottom")

		# each field has 5 bubbles so loop in batches of 5
		for (question, i) in enumerate(np.arange(0, len(column2), 5)):
			contours, _ = cutils.sort_contours(column2[i:i + 5])
			bubbled = ""

			for (j, c) in enumerate(contours):
				mask = np.zeros(answersContour.shape, dtype="uint8")
				cv.drawContours(mask, [c], -1, 255, -1)
				mask = cv.bitwise_and(answersContour, answersContour, mask=mask)
				total = cv.countNonZero(mask)

				# if ~50% bubbled count as marked
				if total > 1700:
					bubbled += chr(j + 65)
				# count as unsure
				elif total > 1000:
					bubbled = '?'
					self.unsure.append(question + 26)
					self.images.append(self.getImageSlice(question + 26, minY, maxY, self.answersOffset))
					break

			self.answers.append(bubbled)

	def gradeVersion(self, versionContour):
		# find bubbles in version box
		_, allContours, _ = cv.findContours(versionContour, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		versionContours = []

		for contour in allContours:
			(x, y, w, h) = cv.boundingRect(contour)
			aspectRatio = w / float(h)

			if w >= 45 and h >= 45 and aspectRatio >= 0.9 and aspectRatio <= 1.1:
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
			aspectRatio = w / float(h)

			if w >= 45 and h >= 45 and aspectRatio >= 0.9 and aspectRatio <= 1.1 and self.idInBounds(x, y):
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