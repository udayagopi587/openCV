#Thresholding:- It's a process of binarising the image. That is comparing the each pixel with a threshold value and if pixel < threshold then that pixel is considered
#as 0, if it is > then it will be considered either as 1 or 255.

import cv2 as cv
import numpy as np

img = cv.imread('images\lady.jpg')

cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('LadyGray', gray)

# Two types of thresholding.

# Method:- 1 Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

print(threshold)

cv.imshow('Thresholded Image', thresh)

#Inverse Threshold

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

print(threshold)

cv.imshow('Inverse Thresholded Image', thresh_inv)

#In the simple threshold technique, the threshold value is user defined, hence this type of threshold may work for some cases and may not work for some other cases.

# Hence, in the adaptive threshold technique the algorithm it self finds the appropriate threshold value.

# Method:- 2 Adaptive Thresholding.

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

#Here 11 is the kernal size to find  the mean, so it is 11x11, and the 3 is just an integer which will be subtracted from the mean. In place of MEAN we can also use GUASSIAN.

cv.imshow('Adaptive Threshold Image', adaptive_threshold)


cv.waitKey(0)
