import cv2 as cv
import cvzone
import numpy as np
import mediapipe as mp
import math as m

class HandDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self,img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo = 0, draw = True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 3, (0, 0, 255), cv.FILLED)
        return lmlist


#The above class is copied from git

class DragRect():
    def __init__(self, posCenter, size=[200,200]):
        self.posCenter = posCenter
        self.size = size

class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and \
                cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor


rectList = []
for x in range(5):
    rectList.append(DragRect([x * 250 + 150, 150]))

capture = cv.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)  #Setting the image resolution.
color_rect = (32, 0, 128)
cx,cy,w,h = 100,100,300,300 #Rect co-ords
hand_detect = HandDetector(detectionCon = 0.8) #By default it should be 0.5, so trying for accurate hand detection.


while True:
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1) #2,Fliping the frame(in the output it is mirroring so..) 0 for vertical flip, 1 for horizontal flip.
    hand = hand_detect.findHands(frame) #1,Detecting the hand in real time.
    lmList = hand_detect.findPosition(hand) #1,Grabing landmarks for locating the position of fingers so which can be hepful for drag; boundbox(bb)
    #4,Now, the moto is to check whether the hand is present in the landmark list, if so, need to find the tip of the index finger and also need to check if it is in the middle of rectangle or not
    #.. refer https://google.github.io/mediapipe/solutions/hands.html for location of fingers. lmList[8] = index finger position from mediapipe lib

    #5. First, need to check whether the finger is at the center or not; 2nd need to check whether we clicked (bringing index and middle finger close) or not for dragging.


    if len(lmList) != 0:
            #print(lmList[8], lmList[12])
            x1, y1 = lmList[8][0], lmList[8][1]
            x2, y2 = lmList[12][0], lmList[12][1] #Found out the position of tip of index and middle finger.
            cx_line, cy_line = (x1+x2)//2, (y1+y2)//2  #FInding the center of the line.
            
            cv.circle(frame, (x1,y1), 5, (255,0,0), cv.FILLED) 
            cv.circle(frame, (x2,y2), 5, (255,0,0), cv.FILLED)
            cv.line(frame, (x1,y1), (x2,y2), (0,0,255), 2)
            cv.circle(frame, (cx_line,cy_line), 5, (255,0,255), cv.FILLED) #Circle created at the center of the line.
            length = m.hypot(x2-x1, y2-y1) #Length of the line
            print(length)

            if length < 45:
                cv.circle(frame, (cx_line,cy_line), 5, (255,255,255), cv.FILLED)


    if lmList:
        
        if length < 45:
            cursor = lmList[8]

            #Call the update here.
            for rect in rectList:
                rect.update(cursor)


            #print(f' lm list {lmList[8]}')
            #print(cursor[1]) #Debug
            #if ((cx-w)//2<cursor[0]<(cx+w)//2) and ((cx-h)//2<cursor[1]<(cx+h)//2): #cursor[0] = rectangle x limits, 1 for y limits #6, changed to dynamic vals
            #    print('Position is OK') #Debug
            #    color_rect = (0,0,255)
            #    cx, cy = cursor[0], cursor[1] #This is for changing the position of rect once after detected by the index finger
            #    print(cursor)
            #else:
            #    color_rect = (0, 255, 0)

            #Need to find the dist between index, middle; if lesser dist then it is considered as click. <<<< HALT >>> 

        


    #cv.rectangle(frame, (100,100), (300,300), color_rect, cv.FILLED) #3,Creating a rectangle for drag and drop
        imgNew = np.zeros_like(frame, np.uint8)
        for rect in rectList:
            cx, cy = rect.posCenter
            w, h = rect.size
            cv.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                          (cx + w // 2, cy + h // 2), color_rect, cv.FILLED)
            cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

        out = frame.copy()
        alpha = 0.01
        mask = imgNew.astype(bool)
        out[mask] = cv.addWeighted(frame, alpha, imgNew, 1 - alpha, 0)[mask]
                #6, changing to dynamic vals.
        cv.imshow('Video', out)
        if cv.waitKey(20) & 0xFF==ord('d'): 
            break  
capture.release() 
cv.distroyAllWindows()



