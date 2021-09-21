# Histograms allow us to visualize the distribution of pixel intensity in any image.

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

#mask = cv.bitwise_and(gray,gray,mask=circle)
#cv.imshow('Mask', mask)

#GRayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

#<SYNTAX> :- cv2.calcHist(images, channels, mask, histSize, ranges)

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

# Colour Histogram

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img,img,mask=mask)

cv.imshow('Masked', masked)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    #print(enumerate(colors))
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)

