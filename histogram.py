import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Red_Apple.jpg")

img0 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
th = cv.inRange(img0,230,255)
th = cv.bitwise_not(th)
#plt.hist(img0.ravel(),256,[0,256])
#plt.show()
cv.imshow("",th)
cv.waitKey(0)

colors = ("b","g","r")
for i,color in enumerate(colors):
    hst = cv.calcHist([img],[i],th,[256],[0,256])
    plt.plot(hst,color = color)
    plt.xlim([0,256])

plt.show()