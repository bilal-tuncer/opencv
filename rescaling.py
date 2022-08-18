
import cv2 as cv
import numpy as np

img = cv.imread("Mixed.jpg")

res = cv.resize(img,(300,400))

cv.imshow("res", res)
cv.waitKey(0)

height, width,chh= res.shape

M = np.float32([[1,0,-30],[0,1,-40]])
dst = cv.warpAffine(res,M,(width, height))
cv.imshow("image",dst)
cv.waitKey(0)

cv.imwrite("shifted.jpg",dst)
print(dst.shape)