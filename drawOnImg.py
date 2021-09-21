import cv2 as cv
import numpy as np

# this example describes about drawing shapes and putting text on an image, the image can be a local image or a black image. Here, will create a blank image.
blank = np.zeros((500,500,3), dtype='uint8') # 'unit8 is the default data type for images. 500,500 is height, width also we can use 500,500,3 this 3 is for no of image channels such as RGB.

#cv.imshow('BlankImage', blank)

##1. Paint the image with a certain colour.

###blank[:] = 0,255,0 #Here setting all the pixcels to Green, blank[:] is referencing all the pixcels,

##    #Here we can even paint only selected portion of the blank image.. Ex:-
##blank[200:300, 300:400 ] = 0,255,0

##cv.imshow("Green", blank)

##2. Draw a rectangle.
#cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=cv.FILLED) #try thickness=2

##<SYNTAX>
#		#	img	=	cv.rectangle(	img, center, radius, color[, thickness[, lineType[, shift]]]	)
#		#	img	Image where the circle is drawn.
#		#center	Center of the circle.
#		#radius	Radius of the circle.
#		#color	Circle color.
#		#thickness	Thickness of the circle outline, if positive. Negative values, like FILLED, mean that a filled circle is to be drawn.
#		#lineType	Type of the circle boundary. See LineTypes
#		#shift	Number of fractional bits in the coordinates of the center and in the radius value.

#cv.imshow("Rectangle", blank)

##3. Draw a circle
#cv.circle(blank, (250,250), 50, (250,0,0), thickness=2) #thickness can be -1, try
#cv.imshow("Circle", blank)

##3. Draw a line
#cv.line(blank, (0,0), (250,250), (255,255,255), thickness=2)
#cv.imshow('Line', blank)

## check this link for more syntax https://docs.opencv.org/3.4.13/d6/d6e/group__imgproc__draw.html


#4. Writing text on image
cv.putText(blank, 'Hello, I am Uday!!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
