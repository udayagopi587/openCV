import cv2 as cv
import numpy as np

img = cv.imread('images\cat.jpg')

cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayCat', gray)

#1. Laplacian Edge Detection :- The laplacian method will find out the edge detection by finding the gradiant between black and white pixels. So, in general there won't be any negative pixel values hence the absolute value is calculated.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) #uint8 is the dtype of any image.
cv.imshow('Laplacian Edge Detection', lap)

#2. Sobel Edge Detection:- Sobel computes the gradient in two directions i.e x and y.

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) #1, 0 is the x direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) #0, 1 is the y direction

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combine_sobel)

#Lets compare the results with Canny

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny) #Canny is the more advanced algorithm and it uses sobel in one of its stages.


cv.waitKey(0)
