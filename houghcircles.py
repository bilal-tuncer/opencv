import cv2 as cv
import numpy as np

img = cv.imread("shapes.jpg",0)
img = cv.pyrDown(img)
img = cv.medianBlur(img,5)
colored_img = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1.5,25,param1=130,param2=110)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    #center circle
    cv.circle(colored_img, (i[0],i[1]),2,(255,0,0),2)
    #outer circle
    cv.circle(colored_img, (i[0],i[1]),i[2],(0,255,0),2)

cv.imshow("img",colored_img)
cv.waitKey(0)
