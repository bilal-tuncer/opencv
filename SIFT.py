import cv2 as cv
import numpy as np

img = cv.imread("Nyork.jpg")
img = cv.pyrDown(img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
keypoints = sift.detect(gray,None)

img=cv.drawKeypoints(gray,keypoints,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("keypoints.jpg",img)
cv.waitKey(0)
