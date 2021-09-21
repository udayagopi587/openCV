#Image Blurring techniques...

#We do smoothing techniques to reduce the noise in the images, the noise can be occured due to camera sensor or lighting or anything.. so we will reduce the mnoise by applying some blurring techs.

import cv2 as cv
import numpy as np

img = cv.imread('images\lady.jpg')

cv.imshow("LadyOriginal", img)

#First we must understand, kernal i.e a portion of an image which is a window/kernal. Basicaly it is a nxn matrix, so the kernal size is "n".
#Now, the blurring is applied on the center pixel of respective kernal, the amount of blurring is effected by the surrounding pixels.

# Method 1:-  Averaging.
#Methodology:- Here, the center pixel intensity is calculated as the average intensity of the other surrounding pixels. The same process will be applied throughout the image.

average = cv.blur(img, (5,5)) #(3,3) is the kernal size, if the size of kernal increases then the blur intensity also increases.
cv.imshow('AverageBlur', average)

# Method 2:- Guassian Blur:- This is similar to the averaging, but instead of assigning the averaging, here this considers the product of each pixel weights. Using this method
# we get less blur than the averaging but it is the more natural blur compared to averaging method.

gaussian = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('GuassianBlur', gaussian) #Ex:- https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/

# Method 3:- Median Blur:- This is same as averaging blur technoque, but here instead of considering the average, median is considered to blur the image.
# This is the more effective method(than avg, gauss) to reduce the noise such as salt and pepper noise. Hence this method is more often used in advance computer vision projects.

median = cv.medianBlur(img, 5) #Here no need to give (3,3), if we just give a integer the openCV will consider it as (3,3); median method is not meant for more kernal size blurring not even 5..
cv.imshow('MedianBlur', median)

# Method 4:- Bilateral Blurring, This is the most effective way of blurring and will be used on vast computer vision projects because of its blurring tech..
# Unless, like the other blurring techniques, bilateral blur tech will retain the edges in the image.

bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('BilateralBlur', bilateral)

# as the sigmaspace, sigmacolor increases it tends to median blur type.

## SYNTAX ##
#bilateralFilter(src, dst, d, sigmaColor, sigmaSpace, borderType)
#This method accepts the following parameters −

#src − A Mat object representing the source (input image) for this operation.

#dst − A Mat object representing the destination (output image) for this operation.

#d − A variable of the type integer representing the diameter of the pixel neighborhood. = 5 nothing but the kernal size

#sigmaColor − A variable of the type integer representing the filter sigma in the color space.

#sigmaSpace − A variable of the type integer representing the filter sigma in the coordinate space.

#borderType − An integer object representing the type of the border used.


cv.waitKey(0)
