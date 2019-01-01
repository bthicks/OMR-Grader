from imutils.perspective import four_point_transform
import fifty_questions
import short_answer
import argparse
import cv2 as cv
import json
import base64

def findPage(im):
	# convert image to grayscale then blur to better detect contours
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
		print('No page found in image')
		exit(0)

	# apply perspective transform to get top down view of page
	return four_point_transform(imgray, page.reshape(4, 2))

def main():
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

	page = findPage(im)
	test = fifty_questions.FiftyQuestionTest(page)
	#test = short_answer.ShortAnswerTest(page)
	answersContour = test.getAnswersContour()
	versionContour = test.getVersionContour()
	idContour = test.getIdContour()

	test.gradeAnswers(answersContour)
	test.gradeVersion(versionContour)
	test.gradeId(idContour)

	answers = test.getAnswers()
	unsure = test.getUnsure()
	images = test.getImages()
	version = test.getVersion()
	studentId = test.getId()

	# encode image slices into base64
	encodedImages = []
	for image in images:
		_, binary = cv.imencode('.png', image)
		encoded = base64.b64encode(binary)
		encodedImages.append(encoded.decode("utf-8"))

	data = {"Student ID" : studentId, "Version" : version, "Answers" : answers, "Unsure" : unsure, "Images" : encodedImages}
	jsonData = json.dumps(data)

	# for debugging
	#for image in images:
	#	cv.imshow("img", image)
	#	cv.waitKey()

	print("answers", answers)
	print("unsure", unsure)
	print("version", version)
	print("id", studentId)

	return jsonData

main()	