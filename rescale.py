import cv2 as cv
img = cv.imread('images/cat.jpg')
cv.imshow('Cat_Normal Size', img)

def rescaleFrame(frame, scale=0.2): #here rescaling the image by 75%.
    #This method will work for image, video and live video.
    width = int(frame.shape[1]*scale) #frame.shape[1] will give width of image by default. similarly frame.shape[0] will give height.
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #this function will do resize of image acc to the given dimensions

image_resize = rescaleFrame(img, scale=0.7) #Although we mentioned 20% in the function definition, the line executed in from the function call only, hence the image is rescaled to 70%..
cv.imshow('Cat_Resized', image_resize)  #Here image has rescaled..

capture = cv.VideoCapture('videos/dog.mp4')  # here the reading will happen using frame by frame

def changeRes(width,height):
    # This method will only work for Live Video
    capture.set(3, width)
    capture.set(4, height) # these 3,4 are default for width and height
while True:
    isTrue, frame = capture.read()  #Here capture.read() will read the video in frame by frame, and the boolean isTrue will return true for successful read
    frame_resized = rescaleFrame(frame) # new function call for resize
    cv.imshow('Video', frame)       #Since this is read frame by frame, seeing the image using imshow, 'Video' is just the window title and passing frame to display the image.
    cv.imshow('Video_Resize', frame_resized)



    if cv.waitKey(20) & 0xFF==ord('d'): #if we conditionally want to close playing the video then this will be used,  after pressing the d this video will end
        break  #this will break the while loop.
capture.release() #realsing the capture pointer.
cv.distroyAllWindows()
