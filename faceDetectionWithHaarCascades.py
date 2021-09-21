#Face Detection:- Detecting the presence of face in a image
#Face Recognition:- Identifying the persons face in an image.

#Face detection is performed by using the classifiers, the classifier essentially detect whether the image is positive or negative, face present or not. All the trained classifiers are available readily.

import cv2 as cv
import numpy as np

img = cv.imread('images\group 2.jpg')
#cv.imshow('Group of 5 ppl', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('Gray Group', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) #Here faces_rect is a rectangle or a list which stores the co-ordinators of the face which were detected by the help of haar classifier.

#**Note:- Haar Cascade is more prone to noise hance it is not the effective way to detect. The more robust output can be achieved by changing the values at "minNeighbors", try with diff images.

#cv.imshow('test', gray)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)