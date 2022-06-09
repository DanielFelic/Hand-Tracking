import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

#Setting time
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0) #Video object instantiation
detector = htm.handDetector()

#Webcam inicialization
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[12])
    #Drawing a landmark
    if id == 12:
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    #Showing FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)