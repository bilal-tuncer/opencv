import numpy as np
import cv2 as cv
import time

img1 = cv.imread("Nyork.jpg")
img2 = cv.imread("Land.jpg")

e1 = cv.getTickCount()
a1 = time.time()
img = cv.add(img1,img2)
e2 = cv.getTickCount()
a2 = time.time()

time1 = a2-a1
t1 = (e2-e1) / cv.getTickFrequency()

print(t1)
print(time1)
print("\n")

cv.imshow("op",img)
cv.waitKey(0)

e1 = cv.getTickCount()
a1 = time.time()
cv.imwrite("Mixed.jpg", img)
e2 = cv.getTickCount()
a2 = time.time()


t2 = (e2-e1) / cv.getTickFrequency()
time2 = a2-a1
print(t2)
print(time2)
