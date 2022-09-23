import cv2 as cv
import numpy as np


im = cv.imread("shapes.jpg")
im = cv.pyrDown(im)
im = cv.pyrDown(im)
img = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
#threshold = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,10)
threshold = cv.inRange(img,200,255)
contours, hierarchy = cv.findContours(threshold, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

dst = cv.drawContours(im, contours,-1, (0,255,0),2)

cv.imshow("a",threshold)
cv.imshow("",dst)
cv.waitKey(0)
