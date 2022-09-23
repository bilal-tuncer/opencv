import cv2 as cv
import numpy as np

img = cv.imread("cars.jpg",0)
img = cv.pyrDown(img)
temp = cv.imread("temp_car.png",0)
temp = cv.pyrDown(temp)
h, w = temp.shape

res = cv.matchTemplate(img,temp,cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = top_left[0]+w,top_left[1]+h

cv.rectangle(img,top_left,bottom_right,255,2)

cv.imshow("res",res)
cv.imshow("1",img)
cv.imshow("2",temp)
cv.waitKey(0)