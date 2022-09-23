import cv2 as cv
import numpy as np

img = cv.imread("bright.jpg",0)
h, w = img.shape
img = cv.resize(img,(int(w/3),int(h/3)))

equ = cv.equalizeHist(img)

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

final = np.vstack((img,equ,cl1))

cv.imshow("",final)
cv.waitKey(0)