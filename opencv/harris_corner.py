import cv2 as cv
import numpy as np

img = cv.imread("chess.jpg")
img = cv.pyrDown(img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
img[dst>0.001*dst.max()]=[0,0,255] 

cv.imshow("",img)
cv.waitKey(0)