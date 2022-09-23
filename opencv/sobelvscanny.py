import cv2 as cv
import numpy as np

def nothing(a):
    pass

if __name__ == "__main__":
    
    img_path = "cars.jpg"
    img = cv.imread(img_path,0)
    img = cv.resize(img,(600,500))

    cv.namedWindow("canny")
    cv.createTrackbar("th1","canny",0,255,nothing)
    cv.createTrackbar("th2","canny",0,255,nothing)
    cv.setTrackbarPos("th1","canny",60)
    cv.setTrackbarPos("th2","canny",100)
    
    cv.namedWindow("sobel")
    cv.createTrackbar("ksize","sobel",1,9,nothing)
    cv.setTrackbarPos("ksize","sobel",1)

    laplacian = cv.Laplacian(img, cv.CV_8U)
    while True:
        th1 = cv.getTrackbarPos("th1","canny")
        th2 = cv.getTrackbarPos("th2","canny")
        sizevalue = cv.getTrackbarPos("ksize","sobel")
        if sizevalue % 2 == 0:
            sizevalue += 1

        sobelx64 = cv.Sobel(img, cv.CV_64F,1,0, ksize = sizevalue)
        sobely64 = cv.Sobel(img, cv.CV_64F,0,1, ksize = sizevalue)
        abs_sobelx64 = abs(sobelx64)
        abs_sobely64 = abs(sobely64)
        sobelx = np.uint8(abs_sobelx64)
        sobely = np.uint8(abs_sobely64)
        sobel = cv.add(sobelx,sobely)
        canny = cv.Canny(img,th1,th2)
        cv.imshow("sobel",sobel)
        cv.imshow("canny",canny)
        cv.imshow("laplacian",laplacian)
        k = cv.waitKey(10)
        if k == 27:
            break
cv.destroyAllWindows()


