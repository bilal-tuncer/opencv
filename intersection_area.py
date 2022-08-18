import cv2 as cv
import numpy as np

img = cv.imread("nike.jpg")

img0 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img0 = cv.inRange(img0,127,255)

black1 = np.zeros(img0.shape,img0.dtype)
black2 = np.zeros(img0.shape,img0.dtype)

contours, hierarchy = cv.findContours(img0,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cnt = contours[2]

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(black1,(x,y),(x+w,y+h),(255,255,255),-1)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(black2,[box],-1,(255,255,255),-1)

intersection_area = cv.bitwise_and(black1,black2)
fcont,fh = cv.findContours(intersection_area,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cv.drawContours(img,fcont,-1,(255,0,0),2)

cv.imshow("1",black1)
cv.imshow("2",black2)
cv.imshow("inter",intersection_area)
cv.imshow("final",img)
cv.waitKey(0)