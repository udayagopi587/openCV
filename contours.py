#Here will look at the contours, although they look similar to edges, but in mathematical representation both the contours and edges are different.
#These contours are very useful while doing shape anaysis and object detection.

#Step for contour detection.
#1. Convert to Gray scale
#2. Find the edges by canny edge detection
#3. Finding contours of the edges, using contours method.


import cv2 as cv
import numpy as np



img = cv.imread('images\cats.jpg')

cv.imshow("OriginalImageCats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank Image", blank)

#RGB2GRAY

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Gray Image", gray)

#blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow("BlurImage", blur)

##Canny Edge Detection

#canny = cv.Canny(blur, 125, 175) #Without blur we have seen 2794 contours. With blur we've seen 380 contours which is 8 times lesser.
#cv.imshow("Canny Edge", canny)

#We even find the contours by using threshould method on a gray image.

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #Here, 125, 255 are the thresholds which means the pixcels below 125 will make as zero and above 255 will be considered as 255 which is 1. Therefore the threshold is a binary conversion.

cv.imshow("Threshold", thresh) #Now, the total are 839 contours.

#in below line pass canny if using canny technique.
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #cv.findContours method will return two o/ps as noted. 
#cv.RETR_LIST returns all the contours, like wise RETR_EXTERNAL this returns the objects external contours, RETR_TREE returns all hierarchical contours.
#APPROX_ gives the approximation of final contours,  NONE will not give any contour approxiamtion so it returns all the contours, APPROX_SIMPLE gives the compressed contours list, ex:-
##if a line is available in the image then the SIMPLE will just return the starting and ending pts of in the returned contour.. this would sufficient for consideration.
#  Since, contours is a list printing the length of it

print(f'{len(contours)} contours found!') ######## WOW !!!!!!!!!!!!!!!!!! So, here we found 2794 contours which is really huge, so now will check the contours by blurring the image. go to blur


#Transferring the contours to a blank image.
cv.drawContours(blank, contours, -1, (0,0,225), 1)
cv.imshow("TranslatedContours", blank)

cv.waitKey(0)
