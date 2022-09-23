import numpy as np
import cv2 as cv


img0 = cv.imread("nike.jpg")
img1 = img0.copy()
img = img0.copy()
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.inRange(img, 127,255)

black = np.zeros(img.shape ,img.dtype)

contours, hierarchy = cv.findContours(img,1,2)
cnt = contours[1]
M = cv.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(img1,(cx,cy),3,(0,0,255),-1)

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(black,(x,y),(x+w,y+h),(255,255,255),2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(black,[box],-1,(255,255,255),2)

bcont, bh = cv.findContours(black, 1,2)
area = cv.contourArea(cv.convexHull(cnt))
big_conts = []
for i in bcont:
    if cv.contourArea(i) > area:
        if not big_conts:
            big_conts.append(i)
        elif cv.contourArea(big_conts[-1]) > cv.contourArea(i):
            big_conts.append(i)

bcnt = big_conts[-1]
cv.drawContours(img0,[bcnt],-1,(0,0,255),2)

big_conts.clear()
for i in bcont:
    if cv.pointPolygonTest(i,(cx,cy),True) > 0:
        if not big_conts:
            big_conts.append(i)
        elif cv.contourArea(big_conts[-1]) > cv.contourArea(i):
            big_conts.append(i)
bcnt = big_conts[-1]
cv.drawContours(img1,[bcnt],-1,(0,0,255),2)

cv.imshow("w_point",img1)
cv.imshow("w_area", img0)
cv.waitKey(0)