import cv2 as cv


img = cv.imread("Red_Apple.jpg")

img = cv.bitwise_not(img)

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("a"):
    cv.imwrite("neg_apple.jpg", img)
