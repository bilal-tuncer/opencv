import cv2 as cv
import numpy as np


img = cv.imread('triangle.jpg',0)
img = cv.inRange(img, 100,255)
kernel = np.ones((2,2),np.uint8)
erosion = cv.erode(img,kernel,iterations = 2)
dilation = cv.dilate(img,kernel,iterations = 2)

noisy = cv.imread("noisy_img.png",0)
#ret,th1 = cv.threshold(noisy,127,255,cv.THRESH_BINARY)
#ret2,th5 = cv.threshold(noisy,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
blur = cv.GaussianBlur(noisy,(3,3),0)
ret3,th6 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
closing = cv.morphologyEx(th6, cv.MORPH_CLOSE, kernel)
opening = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel)
cv.imshow("opneing", opening)
cv.imshow("erode",erosion)
cv.imshow("dilate",dilation)
cv.waitKey(0)
