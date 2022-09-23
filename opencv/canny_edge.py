import cv2 as cv
import numpy as np

def nothing(aa):
    pass

if __name__ == "__main__":

    cap = cv.VideoCapture(0)
    cv.namedWindow("edge")
    cv.createTrackbar("th1","edge",0,255,nothing)
    cv.createTrackbar("th2","edge",0,255,nothing)
    cv.setTrackbarPos("th1","edge",60)
    cv.setTrackbarPos("th2","edge",100)

    while True:

        ret, frame = cap.read()
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        th1 = cv.getTrackbarPos("th1","edge")
        th2 = cv.getTrackbarPos("th2","edge")
        edges = cv.Canny(img,th1,th2)
        laplacian = cv.Laplacian(frame, cv.CV_8U)
        cv.imshow("edge",edges)
        cv.imshow("laplacian", laplacian)
        k = cv.waitKey(10)
        if k == 27:
            break
cv.destroyAllWindows()