import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread("Mixed.jpg")
rows,cols,ch = img.shape
pt1 = np.float32([[0,0],[0,cols],[rows,cols]])
pt2 = np.float32([[40,70], [60,(cols-100)], [(rows-100),(cols-80)]])

M = cv.getAffineTransform(pt1,pt2)

dts = cv.warpAffine(img, M,(cols,rows))

cv.imshow("img",dts)
cv.waitKey(0)

