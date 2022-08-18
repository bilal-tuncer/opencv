import cv2 as cv
import numpy as np


img = cv.imread("sea.jpg")
img = cv.pyrDown(img)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

roi = cv.imread("roisea.jpg")
#roi = cv.resize(img,)
hsvroi = cv.cvtColor(roi,cv.COLOR_BGR2HSV)

histroi = cv.calcHist([hsvroi],[0,1],None,[180,256],[0,180,0,256])

cv.normalize(histroi,histroi,0,255,cv.NORM_MINMAX)
dst = cv.calcBackProject([hsv],[0,1],histroi,[0,180,0,256],1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)

ret,thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(img,thresh)

res = np.vstack((img,res))

cv.imshow("res",res)
cv.waitKey(0)