import cv2 as cv
import numpy as np

img = cv.imread("match_shapes.jpg")

img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

lower = (0,100,100)
upper = (30,255,255)
img = cv.inRange(img,lower,upper)

kernel = np.ones((6,6),np.uint8)
img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
contours, hierarchy = cv.findContours(img,2,1)

m = cv.matchShapes(contours[0],contours[1],1,0.0)
print(m)

cv.imshow("",img)
cv.waitKey(0)