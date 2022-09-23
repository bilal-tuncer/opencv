import numpy as np
import cv2 as cv

img = cv.imread("Nyork.jpg")

new_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow("HSR",new_img)
cv.waitKey(0)