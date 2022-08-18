import cv2 as cv
import numpy as np

img = cv.imread("nike.jpg")
img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
th = cv.inRange(img2,127,255)
#kernel = np.ones((1,1),np.uint8)
#th = cv.morphologyEx(th, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(th, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cnt = contours[2]

cv.drawContours(img,cnt,-1,(0,255,0),2)
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(255,0,0),2)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,150,150),2)

(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(20,200,0),2)

cv.imshow("",img)
cv.waitKey(0)
