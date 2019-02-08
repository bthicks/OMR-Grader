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
import sys, os

class Grader:

    # find and return test page within a given image
    def findPage(self, im):
        # convert image to grayscale then blur to better detect contours
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(imgray.copy(), (5, 5), 0)
        _, threshold = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

        # find contour for entire page 
        _, contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv.contourArea, reverse=True)

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
            return None

        # apply perspective transform to get top down view of page
        return four_point_transform(imgray, page.reshape(4, 2))

    # find and decode QR code in image
    def decodeQR(self, im): 
        _, new_page = cv.threshold(im, 127, 255, cv.THRESH_BINARY)
        decodedObjects = pyzbar.decode(new_page)

        if decodedObjects == []:
            return None
        else:
            return decodedObjects[0]

    # rotate an image by a given angle
    def rotateImage(self, im, angle):
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
    def imageIsUpright(self, page):
        qrCode = self.decodeQR(page)
        qrX = qrCode.rect.left
        qrY = qrCode.rect.top
        qrH = qrCode.rect.height
        w = page.shape[1]
        h = page.shape[0]

        if 0 <= qrX <= (w / 4) and (h / 2) <= qrY <= h:
            return True
        else:
            return False

    # rotate image by 90 degree increments until upright
    def uprightImage(self, page):
        if self.imageIsUpright(page):
            return page
        else:
            for _ in range(3):
                page = self.rotateImage(page, 90)
                if self.imageIsUpright(page):
                    return page
        return None

    # scale values in config dictionary based on width and height of the image 
    # being graded
    def scaleConfig(self, config, width, height):
        x_scale = width / config['page_width']
        y_scale = height / config['page_height']

        for key, val in config.items():
            if 'x' in key or key == 'bubble_width':
                config[key] = val * x_scale
            elif 'y' in key or key == 'bubble_height':
                config[key] = val * y_scale

        return config

    # encode .png image into a base64 string
    def encodeImage(self, image):
        _, binary = cv.imencode('.png', image)
        encoded = base64.b64encode(binary)
        return encoded.decode("utf-8")

    def grade(self, image_name):
        # for debugging
        #cv.namedWindow(image_name, cv.WINDOW_NORMAL)
        #cv.resizeWindow(image_name, 850, 1100)

        # initialize dictionary to be returned
        data = {'studentId' : '', "version" : '', 'answers' : [], 'unsure' : [],
        'images' : [], 'status' : 'success', 'error' : '', 'testImage' : ''}

        # load image 
        im = cv.imread(image_name)
        if im is None:
            data['status'] = 'failure'
            data['error'] = 'Image', image_name, 'not found'
            return json.dump(data, sys.stdout);
        else:
            data['testImage'] = '' #self.encodeImage(im)

        # find test page within image
        page = self.findPage(im)
        if page is None:
            data['status'] = 'failure'
            data['error'] = 'Page not found in', image_name
            return json.dump(data, sys.stdout);

        # decode QR code, which will contain path to configuration file
        qrCode = self.decodeQR(page)
        if qrCode is None:
            data['status'] = 'failure'
            data['error'] = 'QR code not found'
            return json.dump(data, sys.stdout);
        else:
            qrData = qrCode.data.decode('utf-8')
            qrData = os.path.dirname(os.path.abspath(sys.argv[0]))+'/config/6q.json'

        # read config file into dictionary and scale values
        try:
            with open(os.path.dirname(os.path.abspath(sys.argv[0]))+'/config/6q.json') as file:
                config = json.load(file)
            config = self.scaleConfig(config, page.shape[1], page.shape[0])
        except FileNotFoundError:
            data['status'] = 'failure'
            data['error'] = 'Configuration file', qrData, 'not found'
            return json.dump(data, sys.stdout);

        # rotate page until upright
        page = self.uprightImage(page)
        if page is None:
            data['status'] = 'failure'
            data['error'] = 'Could not upright page in', image_name
            return json.dump(data, sys.stdout);

        # create test object
        test = short_answer.ShortAnswerTest(page, config)

        # find answers box and grade bubbles
        answersContour = test.getAnswersContour()
        if answersContour is None:
            data['status'] = 'failure'
            data['error'] = 'Answers contour not found'
        else:
            test.gradeAnswers(answersContour)
            data['answers'] = test.getAnswers()

        # find version box and grade bubbles
        versionContour = test.getVersionContour()
        if versionContour is None:
            data['status'] = 'failure'
            data['error'] = 'Version contour not found'
        else:
            test.gradeVersion(versionContour)
            data['version'] = test.getVersion()

        # find id box and grade bubbles
        idContour = test.getIdContour()
        if idContour is None:
            data['status'] = 'failure'
            data['error'] = 'ID contour not found'
        else:
            test.gradeId(idContour)
            data['studentId'] = test.getId()

        # encode image slices into base64
        encodedImages = []
        for image in test.getImages():
            encodedImages.append(encodeImage(image))

        data['unsure'] = test.getUnsure()
        data['images'] = encodedImages
        
        # for debugging
        #for image in images:
        #    cv.imshow("img", image)
        #    cv.waitKey()

        #print("answers", answers)
        #print("unsure", unsure)
        #print("version", version)
        #print("id", studentId)   

        return json.dump(data, sys.stdout);

def main():
    # parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = vars(ap.parse_args())

    # grade test
    grader = Grader()
    return grader.grade(args["image"]) 

if __name__ == "__main__":
    main()
