import cv2 as cv
from cv2 import cvtColor
import numpy as np

cap = cv.VideoCapture("havuz.avi")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    img = frame.copy()
    img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lower = (20,110,110)
    upper = (40,255,255)
    img = cv.inRange(img,lower,upper)
    contours, hierarchy = cv.findContours()
    
    cv.imshow("frame",img)
    k = cv.waitKey(10)
    if k == 27:
        break
cv.destroyAllWindows()