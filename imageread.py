import cv2 as cv

#below is for image read
#img = cv.imread('images/cat_large.jpg') #Here we have just given the sub path since both the program and this image is in same directory, else we must give full path.

#cv.imshow('Cat', img)

#cv.waitKey(0)

#Below is for Video Capture.; we will read the video by using a method called cv.VideoCapture, and the instance is capture.

capture = cv.VideoCapture('videos/dog.mp4')  # here the reading will happen using frame by frame; inside () we can pass 0,1,2; 0 is default for web cam..
while True:
    isTrue, frame = capture.read()  #Here capture.read() will read the video in frame by frame, and the boolean isTrue will return true for successful read
    cv.imshow('Video', frame)       #Since this is read frame by frame, seeing the image using imshow, 'Video' is just the window title and passing frame to display the image.

    if cv.waitKey(20) & 0xFF==ord('d'): #if we conditionally want to close playing the video then this will be used,  after pressing the d this video will end
        break  #this will break the while loop.
capture.release() #realsing the capture pointer.
cv.distroyAllWindows()

# here after playing, suddenly stops playing and thrown this error i.e error: (-215:Assertion failed), this is because the openCV couldn't find any video in the specified location. Reason:- The openCV ran out of frames to read.
