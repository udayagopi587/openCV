# This will help to focus only on a certairn area in the image, such as focusing only on face in full picture.
# Makes sure that the dimension of mask must be same as the dimension of image.


import cv2 as cv
import numpy as np

img = cv.imread('images\cats.jpg')
cv.imshow('OriginalImage', img)

blank = np.zeros(img.shape[:2], dtype='uint8') #Image and Mask has same image.

cv.imshow('Blank', blank)

#Creating a mask

#print(img.shape[0])
#print(img.shape[1])
#print(img.shape)

mask = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1) 
#mask = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow('Mask', mask)

#Making the image.

masked_image = cv.bitwise_and(img, img, mask=mask) #It gives the intersection of both images, i.e the common area.
cv.imshow('MaskedImage', masked_image)

cv.waitKey(0)