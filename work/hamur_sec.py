import cv2 as cv
import numpy as np

def nothing(aa):
    pass


cv.namedWindow("cam")
cv.createTrackbar('minH, minB','cam',0,255,nothing)
cv.createTrackbar('maxH, maxB','cam',0,255,nothing)
cv.createTrackbar('minS, minG','cam',0,255,nothing)
cv.createTrackbar('maxS, maxG','cam',0,255,nothing)
cv.createTrackbar('minV, minR','cam',0,255,nothing)
cv.createTrackbar('maxV, maxR','cam',0,255,nothing)
cv.setTrackbarPos("minH, minB",'cam',0)
cv.setTrackbarPos('maxH, maxB','cam',255)
cv.setTrackbarPos('maxS, maxG','cam',255)
cv.setTrackbarPos('maxV, maxR','cam',255)

frame = cv.imread("/home/bil/Documents/Rakamlar/0/0_0/photo-1663832565581.jpg")
frame = cv.GaussianBlur(frame,(5,5),1)
while True:
    
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv = frame
    minH = cv.getTrackbarPos('minH, minB','cam')
    maxH = cv.getTrackbarPos('maxH, maxB','cam')
    minS = cv.getTrackbarPos('minS, minG','cam')
    maxS = cv.getTrackbarPos('maxS, maxG','cam')
    minV = cv.getTrackbarPos('minV, minR','cam')
    maxV = cv.getTrackbarPos('maxV, maxR','cam')

    lower_bound = np.array([minH,minS,minV])
    upper_bound = np.array([maxH,maxS,maxV])

    mask = cv.inRange(hsv , lower_bound, upper_bound)

    cleanmask = mask.copy()
    #kernel = np.ones((4,4),np.uint8)
    #mask = cv.dilate(mask,kernel,iterations = 6)
    #mask = cv.erode(mask,kernel,iterations = 6)

    mask = cv.bitwise_not(mask)
    res = cv.bitwise_and(frame,frame,mask= mask)
    miniframe = cv.resize(res,[int(frame.shape[1]/8),int(frame.shape[0]/8)])
    minimask = cv.resize(mask,[int(frame.shape[1]/8),int(frame.shape[0]/8)])
    miniclean = cv.resize(cleanmask,[int(frame.shape[1]/8),int(frame.shape[0]/8)])
    #cv.imshow('frame',frame)
    cv.imshow('mask',minimask)
    cv.imshow('cam',miniframe)
    #cv.imshow("cleanmask",miniclean)
    k = cv.waitKey(50)
    if k == ord("s"):
        print("write")
        cv.imwrite("/home/bil/git_code/work/test/newSS.jpg", res)
    if k == 27:
        break
cv.destroyAllWindows()