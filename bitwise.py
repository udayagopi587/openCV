# Deals with Bitwise operators in OpenCV.
# The bit wise operators will be more useful while doing maskings. These operate on a binary manner so the pixel is turned off when it is 0 and turned on when
# it is 1.

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# BITWISE AND --> Intersecting Regions

bitwise_and = cv.bitwise_and(rectangle, circle) #It gives the intersection of both images, i.e the common area.
cv.imshow('BITWISE_AND', bitwise_and)

# BITWISE OR --> Non-intersecting and intersecting regions; so total.
bitwise_or = cv.bitwise_or(rectangle, circle) #It gives both the area, like super impose of both images.
cv.imshow('BITWISE_OR', bitwise_or)

# BITWISE XOR --> Non-intersecting regions; XOR = OR - AND

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('BITWISE_XOR', bitwise_xor)

# BOTWISE NOT --> It doen't return anything, but it inverts the binary column.

bitwise_not = cv.bitwise_not(rectangle) #It allows on image.
cv.imshow('BITWISE_NOT', bitwise_not)



cv.waitKey(0)
