import cv2 as cv
import numpy as np

def nothing(aa):
    pass

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cv.namedWindow("cam")
cv.createTrackbar('minH','cam',0,255,nothing)
cv.createTrackbar('maxH','cam',0,255,nothing)
cv.createTrackbar('minS','cam',0,255,nothing)
cv.createTrackbar('maxS','cam',0,255,nothing)
cv.createTrackbar('minV','cam',0,255,nothing)
cv.createTrackbar('maxV','cam',0,255,nothing)
cv.setTrackbarPos('maxH','cam',255)
cv.setTrackbarPos('maxS','cam',255)
cv.setTrackbarPos('maxV','cam',255)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    minH = cv.getTrackbarPos('minH','cam')
    maxH = cv.getTrackbarPos('maxH','cam')
    minS = cv.getTrackbarPos('minS','cam')
    maxS = cv.getTrackbarPos('maxS','cam')
    minV = cv.getTrackbarPos('minV','cam')
    maxV = cv.getTrackbarPos('maxV','cam')

    lower_bound = np.array([minH,minS,minV])
    upper_bound = np.array([maxH,maxS,maxV])

    mask = cv.inRange(hsv , lower_bound, upper_bound)

    res = cv.bitwise_and(frame,frame,mask= mask)

    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    cv.imshow('cam',res)
    k = cv.waitKey(10)
    if k == ord("s"):
        cv.imwrite("newSS.jpg", res)
    if k == 27:
        break
cv.destroyAllWindows()