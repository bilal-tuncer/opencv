import cv2 as cv
import numpy as np

tx = 0
ty = 0
draw = False

def drectangle(event,x,y,flag,param):
    global tx
    global ty
    global img
    global draw

    if event == cv.EVENT_LBUTTONDOWN:
        tx = x
        ty = y
        draw = True
    if event == cv.EVENT_MOUSEMOVE and draw:
        img = img0.copy()
        cv.rectangle(img,(tx,ty),(x,y),(0,0,255),2)
    if event == cv.EVENT_LBUTTONUP:
        draw = False
    

img0 = cv.imread("cars.jpg")
img0 = cv.pyrDown(img0)
img = img0.copy()
cv.namedWindow("window")
cv.setMouseCallback("window",drectangle)
while True:
    cv.imshow("window",img)
    k = cv.waitKey(10)
    if k == 27:
        break
cv.destroyAllWindows()
