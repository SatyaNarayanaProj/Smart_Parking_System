import cv2
import numpy as np
import math
from parking import storage as book

count = 100

rectW,rectH=107,48

cap=cv2.VideoCapture(0)

posList = []
for i in range(5):
    posList.append((100, 50 + math.ceil(i * rectH * 1.25)))
    posList.append((300, 50 + math.ceil(i * rectH * 1.25)))

frame_counter = 0
def check(imgPro):
    spaceCount=0
    # if count == 0:
    #     book.handle()
    alloted=book.getAll()
    for a in range(len(posList)):
        pos = posList[a]
        x,y=pos
        crop=imgPro[y:y+rectH,x:x+rectW]
        count=cv2.countNonZero(crop)
        if str(a) in alloted and count<900:
            color = (0, 255, 247)
        elif count < 900:
            spaceCount += 1
            color = (0, 255, 0)
        else:
            if str(a) in alloted:
                book.remove(a)
            color = (0, 0, 255)

        cv2.rectangle(img,pos,(x+rectW,y+rectH),color,2)
        cv2.putText(img, str(a), (math.floor(pos[0] + (rectW / 2)), math.floor(pos[1] + (rectH / 2))), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color,2)

    cv2.rectangle(img,(20,0),(120,25),(180,0,180),-1)
    cv2.putText(img,f'Free: {spaceCount - 5}/{len(posList) - 5}',(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

while True:
    _,img=cap.read()
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 #Or whatever as long as it is the same as next line
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 0)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(3,3),1)
    Thre=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    blur=cv2.medianBlur(Thre,5)
    kernel=np.ones((3,3),np.uint8)
    dilate=cv2.dilate(blur,kernel,iterations=1)
    count -= 1
    check(dilate)
    if count == 0:
        count = 100
    re = cv2.resize(img, (1920, 1080))
    cv2.namedWindow("Smart Parking Management System", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Smart Parking Management System", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # cv2.imshow("Smart Parking Management System", re)
    cv2.imshow("Smart Parking Management System", img)
    cv2.waitKey(10)
