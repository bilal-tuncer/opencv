import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_name = "shapes.jpg"
img = cv.imread(img_name)
img = cv.pyrDown(img)
img = cv.pyrDown(img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,20,0.01,40)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow("img",img)
cv.waitKey(0)