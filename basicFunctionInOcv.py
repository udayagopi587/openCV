import cv2 as cv

# Read in an image
img = cv.imread('images/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR to Gray scale
cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #Here (3,3) the kernal size is the intensity of blur, can use like (7,7).. for increasing or decreasing
cv.imshow('Blur', blur)

## Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1) #By default the structure passing to the cv.dilate is "canny", and the no.of iterations can be increased or decrese.
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=1) #dilated is passed.
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #Resize either compresses or expand the image with in the specific bound. And the interpolation is used while shrinking the image.
cv.imshow('Resized', resized)

## Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
