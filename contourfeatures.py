import cv2 as cv
import numpy as np

img = cv.imread("star.jpg",0)
img = cv.pyrDown(img)
img = cv.pyrDown(img)

kernel = np.ones((3,3),np.uint8)
img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

ret, th = cv.threshold(img,240,255,cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(th, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cv.imshow("",th)
cv.waitKey(0)
M = cv.moments(contours[0])
print(M)
nimg = img.copy()
nimg = cv.drawContours(nimg, contours,1, (0,255,0),2)
area = cv.contourArea(contours[1])
perimeter = cv.arcLength(contours[1],True)

epsilon = 0.02*perimeter
approx = cv.approxPolyDP(contours[1], epsilon,True)

nimg2 = cv.drawContours(img, [approx],-1, (0,255,0),2)
print(f'Perimeter : {perimeter}')
print("Area : {}".format(area))
print(f'Shape : {img.shape}')
cv.imshow("1",nimg)
cv.imshow("2",nimg2)
cv.waitKey(0)