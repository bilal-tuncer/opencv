import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

path_img = "sudoku.jpg"
W = 600
H = 600
img = cv.imread(path_img,0)
rows, cols = img.shape

img = cv.resize(img, (W,H))

img = cv.medianBlur(img, 3)

th = cv.adaptiveThreshold(img, 255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,17,7)

#th = cv.adaptiveThreshold(img, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,17,5)


cv.imshow("img",th)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("fnl_sudoku.jpg",th)
