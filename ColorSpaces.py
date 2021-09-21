# This describes the color spaces in Open CV.

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#OpenCV reads the image in BGR format, but outside the OpenCV it will be read as RGB. So, wil check the image from a library which is out side of OpenCV i.e matplotlib.

img = cv.imread('images\lady.jpg')
cv.imshow("Lady", img)

#plt.imshow(img)
#plt.show() #so we see color inversion, since matlab read in RGB format.

#BGR to GRAY

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayImage", grey)

#BGR to HSV (Hue saturation value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image", hsv)

#BGR to L*A*B

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB Image", lab)

#BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#plt.imshow(rgb)
#plt.show()

## Color Inversion

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr)


#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB --> BGR", lab_bgr)

cv.waitKey(0)

