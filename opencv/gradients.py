import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("shapes.jpg",0)

sizevalue = 3
laplacian = cv.Laplacian(img, cv.CV_8U)
sobelx8 = cv.Sobel(img, cv.CV_8U,1,0, ksize = sizevalue)
sobely8 = cv.Sobel(img, cv.CV_8U,0,1, ksize = sizevalue)

sobelx64 = cv.Sobel(img, cv.CV_64F,1,0, ksize = sizevalue)
sobely64 = cv.Sobel(img, cv.CV_64F,0,1, ksize = sizevalue)
abs_sobelx64 = abs(sobelx64)
abs_sobely64 = abs(sobely64)
sobelx = np.uint8(abs_sobelx64)
sobely = np.uint8(abs_sobely64)

sobel = cv.add(sobelx,sobely)

images = [laplacian,sobelx8,sobely8,img, sobelx64, sobel]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],cmap = "gray")
    plt.xticks([]), plt.yticks([])
plt.show()

