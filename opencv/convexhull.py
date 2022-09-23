import cv2 as cv
import numpy as np

img0 = cv.imread("star.jpg")


img0 = cv.pyrDown(img0)
img0 = cv.pyrDown(img0)
img = img0.copy()
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

kernel = np.ones((3,3),np.uint8)
img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

ret, th = cv.threshold(img,240,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(th, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt = contours[1]

hull = cv.convexHull(cnt,returnPoints = False)
defects = cv.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img0,start,end,[0,255,0],2)
    cv.circle(img0,far,5,[0,0,255],-1)

#cv.drawContours(img0,hull,-1,(0,255,0),2)

cv.imshow("",img0)
cv.waitKey(0)
