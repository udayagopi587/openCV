#Face recognition using builtin OpenCV function

import os
import cv2 as cv
import numpy as np

people = []

for i in os.listdir(r'C:\Users\udaya\OneDrive\Documents\openCV\faces\train'):  #Listing the directories in the mentioned path.
    people.append(i)

#print(people)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

DIR = r'C:\Users\udaya\OneDrive\Documents\openCV\faces\train'

features = []
labels = [] #This hold list of names for whos faces matches.

def create_train(): #This function, will loop over all the photos in each path.. And grab the face in each path and will add it to the train set. The trainig set will consists of two sets such as features, labels.
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            #Test
            #print(img_path)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            #With above, looping has completed and each image will be converted to gray. Now we need to detect the face
            #Face detection(haar_cascade) is added above.

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]  #This simply focuses on the face in the image as region of interest. Now, lets add this feature to our list, as well as the corresponding lable.
                features.append(faces_roi)
                labels.append(label)

create_train()

print('<------------------ Training Done -------------------->')


#Model training has done correctly.

#print(f'Length of the feature --> {len(features)}')
#print(f'Length of the labels --> {len(labels)}')

#Converting the Features and label list to numpy arrays.

features = np.array(features, dtype=object)
labels = np.array(labels)

# Training the recognizer.

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training the recognizer on the features array and labels array.

face_recognizer.train(features, labels)

# Now, training has completed, lets do recognition.

# But, if we want to use this face recognizer we explicitly need to write/repeate all the code. Hence, OpenCV has provided an alternative to save this file and hence this
# this file can be accessed anywhere with this yml file.

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)

# Done :)



         
