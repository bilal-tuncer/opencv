
import cv2 as cv

cap = cv.VideoCapture("out_video.avi")
fps = cap.get(cv.CAP_PROP_FPS)
frame_wait = int(1000/fps)
if not cap.isOpened():
    print("cannot open video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("exiting")
        break
    cv.imshow("frame",frame)
    k = cv.waitKey(frame_wait)
    if k == 27:
        break