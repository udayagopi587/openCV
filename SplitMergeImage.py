#This will explain about split and merging of color channels.

import cv2 as cv
import numpy as np

img = cv.imread('images\park.jpg')
cv.imshow("Group", img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow("Blank", blank)

b,g,r = cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape) #Here the output is dipicted and displayed as gray scale. In the output image where there is white portion there the corresponding color components are composed highly. the dark portion will have less color components.

#Here, we got the gray images because, each image with RGB components will have 3 channels, so after spiliting the image the channels also got splitted, hence for each component 1 channel has come. And by default gray scale image has 1 channel so the o/p came in gray scale.

#Merging the splitted color channels to get the original image.

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)

#Now, we will try to split the color channel by using a blank image and merge methods to compose in seperate channels.

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("Blue_NEW", blue)
cv.imshow("Green_NEW", green)
cv.imshow("Red_NEW", red)



cv.waitKey(0)