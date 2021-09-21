#Here, will look at the basic transformation techniques of image such as crop, rotate, translation, resizing

import cv2 as cv
import numpy as np

img = cv.imread('images/lady.jpg')

cv.imshow('Lady', img)

#1. Translation:- Fliping the image along x and y axises.

def translate(img, x,y): #here, x,y represents the axis for which the image transfer has to happen.
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) 
    return cv.warpAffine(img, transMat, dimensions) #warpAffine is a builtin translation method.

# -x --> Left shift4
# -y --> Up shift
# x --> Right Shift
# y --> Down shift

translated = translate(img, 100, 100) #Here +100 for x, +100 for y i.e., the image is transferred to the right by 100 pixcels and down by 100 pixcels.
cv.imshow('Translated Image', translated)

#2. Rotation:- ROtating the image by some angle. Open CV allows to rotate at any point.

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2] #The first two values gives the dimensions of any image.

    if rotPoint is None:
        rotPoint = (width//2,height//2) #Since the rotation point is None, here we are rotating along the centre by default.
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #1.0 is the scaling value after rotate.
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) #here if the angle is +ve then it rotates counter clock wise, -ve clockwise.
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90) #ROtating the rotated image.
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing,

resized = cv.resize(img, (800,500), interpolation=cv.INTER_CUBIC) #If we are shrinking the image then we must go for _AREA or if we are enlarging then we must go for _LINEAR or _CUBIC, cubic is slow but o/p will be better.
cv.imshow('Resized', resized) #above (500,500) is the outputfile dimensions.

#Flipping

flip = cv.flip(img, 1)
#syntax --> cv.flip(img_name, flipCode); here if flipcode = 0 then flipping the original image vertically, 1 for flipping horizontally, -1 for vertical and horizontal flip.
cv.imshow('Flipped Image', flip)


#Image cropping
#This is just like slicing the matrices.
crop = img[50:200, 200:300]
cv.imshow('Cropped', crop)

cv.waitKey(0)
