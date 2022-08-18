import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("board.png")
img = cv.resize(img, (300,300))

blur1 = cv.blur(img, (9,9))
blur2 = cv.GaussianBlur(img, (9,9),0)
blur3 = cv.medianBlur(img, 9)
blur4 = cv.bilateralFilter(img, 9,100,100)

images = [blur1, blur2, blur3, blur4]
titles = ["blur1", "blur2", "blur3", "blur4"]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],vmin=0,vmax=240)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
