import cv2 as cv
import numpy as np

img = cv.imread("coins.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,1,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#opening
kernel = np.ones((3,3),np.uint8)
opened = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=1)

#sure background
sbg = cv.dilate(opened,kernel,iterations=2)

#sure foreground
dist = cv.distanceTransform(opened,cv.DIST_L2,5)
ret, sfg = cv.threshold(dist,0.5*dist.max(),255,0)

erosion = cv.erode(opened,kernel,iterations = 11)

sfg = np.uint8(sfg)
region = cv.subtract(sbg,sfg)

ret, markers = cv.connectedComponents(sfg)

markers += 1
markers[region==255] = 0

markers = cv.watershed(img,markers)
img[markers == -1] = (0,0,255)

print(dist[dist>0])
print(len(dist[dist>0]))

dist = np.uint8(dist)
dist = dist.astype("uint8")
cv.imshow("", dist)
cv.waitKey(0)
cv.destroyAllWindows()
