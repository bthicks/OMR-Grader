from imutils.perspective import four_point_transform
from imutils import contours as cutils
import numpy as np 
import argparse
import imutils
import cv2 as cv
import json
import base64

vagueImages = []
questionsMarked = []
vagueQuestions = []
versionMarked = None
idMarked = ""

def inBounds(x, y):
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

def inBoundsVersion(x, y):
	if 160 <= x <= 475 and 10 <= y <= 20:
		return True
	else:
		return False

def inBoundsID(x, y):
	if 40 <= x <= 780 and 15 <= y <= 600:
		return True
	else:
		return False

# crop image slice for undetermined questions
def getImageSlice(questionNum, minY, maxY, offset):
	
	diff = int((maxY - minY) / 25)

	if 1 <= questionNum <= 25:
		return page[(offset + minY + diff * (questionNum - 1)) : (offset + minY + diff * questionNum), 150 : 650]
	elif 26 <= questionNum <= 50:
		return page[(offset + minY + diff * (questionNum - 26)) : (offset + minY + diff * (questionNum - 25)), 675 : 1175]
	else:
		return None

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

(_, offset, _, _) = cv.boundingRect(contours[2])
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
yValues = []

for contour in contours:
	(x, y, w, h) = cv.boundingRect(contour)

	if w >= 45 and h >= 45 and inBounds(x, y):
		questionContours.append(contour)
		tup = (y, h)
		yValues.append(tup)

minY = yValues[len(yValues) - 1][0]
maxY = yValues[0][0] + yValues[0][1]

# grade bubbles in question box
questionContours, _ = cutils.sort_contours(questionContours, method="left-to-right")
length = len(questionContours)
mid = int(len(questionContours) / 2)
column1 = questionContours[0 : mid]
column2 = questionContours[mid : length]

# grade questions 1-25
column1, _ = cutils.sort_contours(column1, method="top-to-bottom")

# each field has 5 bubbles so loop in batches of 5
for (question, i) in enumerate(np.arange(0, len(column1), 5)):
	contours, _ = cutils.sort_contours(column1[i:i + 5])
	bubbled = ""

	for (j, c) in enumerate(contours):
		mask = np.zeros(questionBox.shape, dtype="uint8")
		cv.drawContours(mask, [c], -1, 255, -1)
		mask = cv.bitwise_and(questionBox, questionBox, mask=mask)
		total = cv.countNonZero(mask)

		# if ~50% bubbled, count as marked
		if total > 1700:
			bubbled += chr(j + 65)
		# count as unsure	
		elif total > 1000:
			bubbled = '?'
			vagueQuestions.append(question + 1)
			vagueImages.append(getImageSlice(question + 1, minY, maxY, offset))
			break

	questionsMarked.append(bubbled)

# grade questions 26-50
column2, _ = cutils.sort_contours(column2, method="top-to-bottom")

# each field has 5 bubbles so loop in batches of 5
for (question, i) in enumerate(np.arange(0, len(column2), 5)):
	contours, _ = cutils.sort_contours(column2[i:i + 5])
	bubbled = ""

	for (j, c) in enumerate(contours):
		mask = np.zeros(questionBox.shape, dtype="uint8")
		cv.drawContours(mask, [c], -1, 255, -1)
		mask = cv.bitwise_and(questionBox, questionBox, mask=mask)
		total = cv.countNonZero(mask)

		# if ~50% bubbled count as marked
		if total > 1700:
			bubbled += chr(j + 65)
		# count as unsure
		elif total > 1000:
			bubbled = '?'
			vagueQuestions.append(question + 26)
			vagueImages.append(getImageSlice(question + 26, minY, maxY, offset))
			break;

	questionsMarked.append(bubbled)

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
maxCount = None

for (j, c) in enumerate(versionContours):
	mask = np.zeros(versionBox.shape, dtype="uint8")
	cv.drawContours(mask, [c], -1, 255, -1)
	mask = cv.bitwise_and(versionBox, versionBox, mask=mask)
	total = cv.countNonZero(mask)

	if versionMarked is None or total > maxCount:
		versionMarked = chr(j + 65)
		maxCount = total

# find bubbles in id box
_, contours, _ = cv.findContours(idBox, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
idContours = []

for contour in contours:
	(x, y, w, h) = cv.boundingRect(contour)
	aspectRatio = w / float(h)

	if w >= 45 and h >= 45 and aspectRatio >= 0.9 and aspectRatio <= 1.1 and inBoundsID(x, y):
		idContours.append(contour)

# grade bubbles in id box
idContours, _ = cutils.sort_contours(idContours, method="left-to-right")

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

# encode image slices into base64
encodedImages = []
for img in vagueImages:
	_, binary = cv.imencode('.png', img)
	encoded = base64.b64encode(binary)
	encodedImages.append(encoded.decode("utf-8"))

data = {"Student ID" : idMarked, "Version" : versionMarked, "Answers" : questionsMarked, "Unsure" : vagueQuestions, "Images" : encodedImages}
jsonData = json.dumps(data)

# for debugging
for img in vagueImages:
	cv.imshow("img", img)
	cv.waitKey()

print("answers", questionsMarked)
print("unsure", vagueQuestions)
print("version", versionMarked)
print("id", idMarked)