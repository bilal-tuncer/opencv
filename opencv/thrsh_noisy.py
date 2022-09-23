import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path_img = "noisy_img.png"
img = cv.imread(path_img,0)
img = cv.resize(img, (300,300))

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,19,9)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,19,10)

ret1,th4 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret2,th5 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
blur = cv.GaussianBlur(img,(3,3),0)
ret3,th6 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("original",img)
images = [th1,th2,th3,th4,th5,th6]
#titles = [thresh]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray",vmin=0,vmax=500)
    #plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()