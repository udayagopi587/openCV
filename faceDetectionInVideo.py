# HOME WORK
import cv2 as cv

capture = cv.VideoCapture('video1person.mp4')

def rescaleFrame(frame, scale=0.2): 
    
    width = int(frame.shape[1]*scale) 
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()

    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    print(f'Number of faces found = {len(faces_rect)}')

    #for (x,y,w,h) in faces_rect:
    #    cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    while True:
        isTrue, frame = capture.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_resized = rescaleFrame(frame)
        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame_resized, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        cv.imshow('Video Out', frame_resized)       

        if cv.waitKey(20) & 0xFF==ord('d'): 
            break  
capture.release() 
cv.distroyAllWindows()