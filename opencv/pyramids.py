import cv2 as cv
import numpy as np

img = cv.imread("cars.jpg")

lower = cv.pyrDown(img)
mlower = cv.pyrDown(lower)

temp = cv.pyrUp(mlower)
newBig = cv.pyrUp(temp)

laplacian1 = cv.Laplacian(img,cv.CV_8U)
laplacian2 = cv.Laplacian(lower,cv.CV_8U)
print(img.shape,lower.shape,mlower.shape,newBig.shape)

cv.imshow("lp1",laplacian1)
cv.imshow("lp2",laplacian2)
cv.imshow("resized",newBig)
cv.imshow("big",img)
cv.imshow("small",lower)
cv.imshow("mlower",mlower)

cv.waitKey(0)