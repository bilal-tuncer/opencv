import cv2 as cv
import numpy as np

img = cv.imread("Nyork.jpg", cv.IMREAD_GRAYSCALE)

row, column = img.shape

#M = cv.getRotationMatrix2D(((column-1)/2.0,(row-1)/2.0),90,0.75)
#dst = cv.warpAffine(img , M, (column,row))

dst = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow("image",dst)
cv.waitKey(0)
