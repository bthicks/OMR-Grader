from imutils.perspective import four_point_transform
import fifty_questions
import short_answer
import argparse
import cv2 as cv
import math
import numpy as np 
import json
import base64
import pyzbar.pyzbar as pyzbar

# find and return test page within a given image
def findPage(im):
   # convert image to grayscale then blur to better detect contours
   imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
   blurred = cv.GaussianBlur(imgray.copy(), (5, 5), 0)
   _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

   # find contour for entire page 
   _, contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
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

# find and decode QR code in image
def decodeQR(im): 
   decodedObjects = pyzbar.decode(im)
   return decodedObjects[0]

# rotate an image by a given angle
def rotateImage(im, angle):
    w = im.shape[1]
    h = im.shape[0]
    rads = np.deg2rad(angle)

    # calculate new image width and height
    nw = abs(np.sin(rads) * h) + abs(np.cos(rads) * w)
    nh = abs(np.cos(rads) * h) + abs(np.sin(rads) * w)

    # get the rotation matrix
    rotMat = cv.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, 1)

    # calculate the move from old center to new center combined with the rotation
    rotMove = np.dot(rotMat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))

    # update the translation of the transform
    rotMat[0,2] += rotMove[0]
    rotMat[1,2] += rotMove[1]

    return cv.warpAffine(im, rotMat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv.INTER_LANCZOS4)

# return True if image is upright, based on QR code coordinates
def imageIsUpright(page):
   qrCode = decodeQR(page)
   qrX = qrCode.rect.left
   qrY = qrCode.rect.top
   print("QR X, QR Y:", qrX, qrY)
   qrH = qrCode.rect.height
   w = page.shape[1]

   if 0 <= qrX <= (w / 4) and 0 <= qrY <= (qrH * 4):
      return True
   else:
      return False

# rotate image by 90 degree increments until upright
def uprightImage(page):
   if imageIsUpright(page):
      return page
   else:
      for _ in range(3):
         page = rotateImage(page, 90)
         if imageIsUpright(page):
            return page
   return None

def main():
   # parse the arguments
   ap = argparse.ArgumentParser()
   ap.add_argument("-i", "--image", required=True, help="path to the input image")
   args = vars(ap.parse_args())

   # load image 
   im = cv.imread(args["image"])
   if im is None:
      print('Image', args["image"], 'not found')
      exit(0)

   # for debugging
   cv.namedWindow(args["image"], cv.WINDOW_NORMAL)
   cv.resizeWindow(args["image"], 850, 1100)

   # find test page within image
   page = findPage(im)
   if page is None:
      print('Page not found in', args["image"])
      exit(0)

   # rotate page until upright
   #page = uprightImage(page)
   #if page is None:
   #   print('Could not upright page in', args["image"])
   #   exit(0)

   #qrCode = decodeQR(page)
   #qrData = qrCode.data.decode('utf-8')
   qrData = "6q"

   if qrData == "50q":
      test = fifty_questions.FiftyQuestionTest(page)
   elif qrData == "6q":
      test = short_answer.ShortAnswerTest(page)
   elif qrData is None:
      print('QR code not found')
      exit(0)
   else:
      print('Incorrect QR code found')
      exit(0)

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
   for image in images:
     cv.imshow("img", image)
     cv.waitKey()

   print("answers", answers)
   print("unsure", unsure)
   print("version", version)
   print("id", studentId)   

   return jsonData

main()   