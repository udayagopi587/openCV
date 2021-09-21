import cv2 as cv
import numpy as np
import os
haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = []

for i in os.listdir(r'C:\Users\udaya\OneDrive\Documents\openCV\faces\train'):  #Listing the directories in the mentioned path.
    people.append(i)

##lets load features and labels array.

#features = np.load('features.npy')
#labels = np.load('labels.npy')

# Lets load the source yml file

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\udaya\OneDrive\Documents\openCV\faces\validation\elton\2.jpg') #Image is from validation.. these images are different from the i\p images.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness = 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness = 2)

cv.imshow('Detected Face', img)
cv.waitKey(0)

#After checking multiple trail checks it is understood that the OpenCV inbuilt model for image recognition is not accurate.