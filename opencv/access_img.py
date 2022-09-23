import numpy as np
import cv2 as cv

img = cv.imread("Red_Apple.jpg", cv.IMREAD_COLOR)

print(img[10,10])

print(img.item(10,10,0))

print(img.shape)

b = img[:,:,0]

print(b.shape)

b,g,r = cv.split(img)

empty = np.zeros(img.shape, img.dtype)
#cv.imshow("empty",empty)
blue  = empty.copy()
green = empty.copy()
red = empty.copy()

blue[:,:,0] = b
green[:,:,1] = g
red[:,:,2] = r

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
cv.waitKey(0)
img = cv.merge((b,g,r))