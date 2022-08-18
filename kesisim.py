import cv2 as cv
import numpy as np

img = cv.imread("nike.jpg")

img0 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img0 = cv.inRange(img0,127,255)

black1 = np.zeros(img.shape,img.dtype)
black2 = np.zeros(img.shape,img.dtype)

contours, hierarchy = cv.findContours(img0,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
cnt = contours[2]

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(black1,(x,y),(x+w,y+h),(255,0,0),2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(black2,[box],0,(0,0,255),2)
#cv.drawContours(img,cnt,-1,(0,255,0),2)

kes = cv.add(black1,black2)

lower = (254,0,254)
upper = (255,1,255)
points = cv.inRange(kes,lower,upper)

pts, hr = cv.findContours(points,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
pointarr = []
for i in pts:
    M = cv.moments(i)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    pointarr.append([cx,cy])

print(pointarr)

nparray = np.int32(pointarr)
print(nparray)
nparray = nparray.reshape((-1,1,2))

hull = cv.convexHull = (nparray)
cv.drawContours(img,[hull],-1,(0,255,255),2)
#cv.polylines(img,[nparray],False,(0,255,255),2)

cv.imshow("1",black1)
cv.imshow("2",black2)
cv.imshow("",kes)
cv.imshow("kesisim",points)
cv.imshow("img",img)
cv.waitKey(0)