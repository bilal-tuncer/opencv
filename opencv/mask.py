import cv2 as cv
import numpy as np

logo = cv.imread("logo.png")
img = cv.imread("Red_Apple.jpg")

row,clm,cha = logo.shape
pla = img[200:row+200,200:clm+200]

graylogo = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
ret ,mask = cv.threshold(graylogo , 150, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
res1 = cv.bitwise_and(pla,pla,mask =mask)
res2 = cv.bitwise_and(logo,logo,mask =mask_inv)
res = cv.add(res1, res2)

img[200:row+200,200:clm+200] = res

img = cv.pyrDown(img)
cv.imshow("mask",img)
cv.waitKey(0)