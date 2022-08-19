import cv2 as cv
import numpy as np

path = "flower.jpg"
img = cv.imread(path)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#this function is not included in default opencv library
surf = cv.xfeatures2d.SURF_create(400)
kp = surf.detect(gray,None)

print(len(kp))