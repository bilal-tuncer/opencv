import cv2 as cv
import numpy as np

if __name__ == "__main__":
    cap = cv.VideoCapture("sample.mp4")
    fps = cap.get(cv.CAP_PROP_FPS)
    wait = int(1000/fps)
    while(True):
        ret, frame = cap.read()
        if not ret:
            break
        cv.imshow("frame",frame)
        cv.waitKey(wait)