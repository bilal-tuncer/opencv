import cv2 as cv
import numpy as np

img = cv.imread('sudoku_paper.jpg')
img2 = img.copy()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,100,150,apertureSize = 3)
lines = cv.HoughLines(edges,1,np.pi/180,130)
lines2 = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines2:
    x1,y1,x2,y2 = line[0]
    cv.line(img2,(x1,y1),(x2,y2),(0,255,0),2)


for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv.imshow("canny",edges)
cv.imshow("img",img)
cv.imshow("P img",img2)
cv.waitKey(0)