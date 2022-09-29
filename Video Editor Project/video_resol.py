import cv2 as cv
import numpy as np
from PIL import Image

if __name__ == "__main__":
    
    video_path = "sample.mp4"
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Cannot open")
        exit()
    fps = cap.get(cv.CAP_PROP_FPS)
    print(fps)
    frame_wait = int(1000/fps)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter("resolution.avi", fourcc, fps, (640,480))

    while True:

        ret, frame = cap.read()
        if not ret:
            print("exiting")
            break

        org_size = (frame.shape[1],frame.shape[0])
        rate = 0.5
        new_size = (int(org_size[0]*rate),int(org_size[1]*rate))
        #frame = cv.resize(frame,new_size)
        #frame = cv.resize(frame,org_size)
        out.write(frame)
        #cv.imshow("frame",frame)
        #if cv.waitKey(frame_wait) == 27:
        #    break
    
    cap.release()
    out.release()
    cv.destroyAllWindows()

