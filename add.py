import numpy as np
import cv2 as cv

img1 = cv.imread("Red_Apple.jpg")
img2 = cv.imread("Land.jpg")

row, clm, channel = img2.shape

#newimg = cv.add(img1[0:row,0:clm,:],img2)
img1[:row,:clm,:] = cv.add(img2,img1[:row,:clm,:])

cv.imshow("add", img1)
cv.waitKey(0)