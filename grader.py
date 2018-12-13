from imutils.perspective import four_point_transform
from imutils import contours as cutils
import numpy as np 
import argparse
import imutils
import cv2 as cv
import json

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load image, convert to grayscale, blur, 
im = cv.imread(args["image"])
if im is None:
	print('Could not find the image:', args["image"])
	exit(0)

# for debugging
#cv.namedWindow(args["image"], cv.WINDOW_NORMAL)
#cv.resizeWindow(args["image"], 850, 1100)

imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(imgray.copy(), (5, 5), 0)
edged = cv.Canny(blurred, 75, 200)

# find contour for entire page
_, contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv.contourArea, reverse=True)
page = None

if len(contours) > 0:
	# approximate the contour
	for contour in contours:
		peri = cv.arcLength(contour, True)
		approx = cv.approxPolyDP(contour, 0.02 * peri, True)

		# verify that contour has four corners
		if len(approx) == 4:
			page = approx
			break
		
else:
	print('No page found in image:', args["image"])
	exit(0)

# apply perspective transform to get top down view of page
page = four_point_transform(imgray, page.reshape(4, 2))

# threshold the page and find boxes within the page
_, threshold = cv.threshold(page, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
_, contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv.contourArea, reverse=True)

peri = cv.arcLength(contours[2], True)
approx = cv.approxPolyDP(contours[2], 0.02 * peri, True)
questionBox = four_point_transform(threshold, approx.reshape(4, 2))

peri = cv.arcLength(contours[14], True)
approx = cv.approxPolyDP(contours[14], 0.02 * peri, True)
versionBox = four_point_transform(threshold, approx.reshape(4, 2))

peri = cv.arcLength(contours[5], True)
approx = cv.approxPolyDP(contours[5], 0.02 * peri, True)
idBox = four_point_transform(threshold, approx.reshape(4, 2))

# find bubbles in question box
_, contours, _ = cv.findContours(questionBox, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
questionContours = []

def inBounds(x, y):
	if y >= 70 and y <= 1745:
		# within left column bounds
		if x >= 180 and x <= 500:
			return True
		# within right column bounds
		elif x >= 705 and x <= 1045:
			return True
		else:
			return False
	else:
		return False 

for contour in contours:
	(x, y, w, h) = cv.boundingRect(contour)

	if w >= 45 and h >= 45 and inBounds(x, y):
		questionContours.append(contour)

# grade bubbles in question box
questionContours, _ = cutils.sort_contours(questionContours, method="left-to-right")
length = len(questionContours)
mid = int(len(questionContours) / 2)
column1 = questionContours[0 : mid]
column2 = questionContours[mid : length]
questionsMarked = []

# grade questions 1-25
column1, _ = cutils.sort_contours(column1, method="top-to-bottom")

# each field has 5 bubbles so loop in batches of 5
for (question, i) in enumerate(np.arange(0, len(column1), 5)):
	contours, _ = cutils.sort_contours(column1[i:i + 5])
	bubbled = ""

	for (j, c) in enumerate(contours):
		mask = np.zeros(questionBox.shape, dtype="uint8")
		mask = cv.bitwise_and(questionBox, questionBox, mask=mask)
		total = cv.countNonZero(mask)

		# if ~50% bubbled, count as marked
		if total > 1000:
			bubbled += chr(j + 65)

	questionsMarked.append(bubbled)

# grade questions 26-50
column2, _ = cutils.sort_contours(column2, method="top-to-bottom")

# each field has 5 bubbles so loop in batches of 5
for (question, i) in enumerate(np.arange(0, len(column2), 5)):
	contours, _ = cutils.sort_contours(column2[i:i + 5])
	bubbled = ""

	for (j, c) in enumerate(contours):
		mask = np.zeros(questionBox.shape, dtype="uint8")
		mask = cv.bitwise_and(questionBox, questionBox, mask=mask)
		total = cv.countNonZero(mask)

		# if ~50% bubbled count as marked
		if total > 1000:
			bubbled += chr(j + 65)

	questionsMarked.append(bubbled)

print("answers", questionsMarked)

# find bubbles in version box
_, contours, _ = cv.findContours(versionBox, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
versionContours = []

for contour in contours:
	(x, y, w, h) = cv.boundingRect(contour)
	aspectRatio = w / float(h)

	if w >= 45 and h >= 45 and aspectRatio >= 0.9 and aspectRatio <= 1.1:
		versionContours.append(contour)

# grade bubbles in version box
versionContours, _ = cutils.sort_contours(versionContours, method="left-to-right")
versionMarked = None
maxCount = None

for (j, c) in enumerate(versionContours):
	mask = np.zeros(versionBox.shape, dtype="uint8")
	cv.drawContours(mask, [c], -1, 255, -1)
	mask = cv.bitwise_and(versionBox, versionBox, mask=mask)
	total = cv.countNonZero(mask)

	if versionMarked is None or total > maxCount:
		versionMarked = chr(j + 65)
		maxCount = total

print("version", versionMarked)

# find bubbles in id box
_, contours, _ = cv.findContours(idBox, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
idContours = []

for contour in contours:
	(x, y, w, h) = cv.boundingRect(contour)
	aspectRatio = w / float(h)

	if w >= 45 and h >= 45 and aspectRatio >= 0.9 and aspectRatio <= 1.1:
		idContours.append(contour)

# grade bubbles in id box
idContours, _ = cutils.sort_contours(idContours, method="left-to-right")
idMarked = ""

# each field has 10 possibilities so loop in batches of 10
for (q, i) in enumerate(np.arange(0, len(idContours), 10)):
	contours, _ = cutils.sort_contours(idContours[i:i + 10], method="top-to-bottom")
	bubbled = None
	maxCount = None

	for (j, c) in enumerate(contours):
		mask = np.zeros(idBox.shape, dtype="uint8")
		cv.drawContours(mask, [c], -1, 255, -1)
		mask = cv.bitwise_and(idBox, idBox, mask=mask)
		total = cv.countNonZero(mask)

		if bubbled is None or total > maxCount:
			bubbled = j
			maxCount = total

	idMarked += str(bubbled)

print("id", idMarked)

data = {"Student ID" : idMarked, "Version" : versionMarked, "Answers" : questionsMarked}
jsonData = json.dumps(data)