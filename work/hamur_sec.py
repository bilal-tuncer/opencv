import cv2 as cv
import numpy as np

def nothing(aa):
    pass


cv.namedWindow("cam")
cv.createTrackbar('minH','cam',0,255,nothing)
cv.createTrackbar('maxH','cam',0,255,nothing)
cv.createTrackbar('minS','cam',0,255,nothing)
cv.createTrackbar('maxS','cam',0,255,nothing)
cv.createTrackbar('minV','cam',0,255,nothing)
cv.createTrackbar('maxV','cam',0,255,nothing)
cv.setTrackbarPos("minH",'cam',5)
cv.setTrackbarPos('maxH','cam',30)
cv.setTrackbarPos('maxS','cam',255)
cv.setTrackbarPos('maxV','cam',255)

frame = cv.imread("/home/bil/git_code/work/Rakamlar(cutted)/0/0_1/photo-1663833351517.jpg")
frame = cv.GaussianBlur(frame,(5,5),1)
while True:
    
    
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