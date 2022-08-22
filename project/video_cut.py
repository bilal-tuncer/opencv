import cv2 as cv
import numpy as np
from PIL import Image

def minutes_to_second(m):
    s = int((100*m) % (100))
    m = int(m-m%1)
    return m*60 + s

if __name__ == "__main__":
    
    video_path = "sample.mp4"
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        print("Cannot open")
        exit()
    fps = cap.get(cv.CAP_PROP_FPS)
    print(fps)
    
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    cut_begin = 0.07
    cut_end = 0.22
    start = minutes_to_second(cut_begin)*int(fps)
    end = minutes_to_second(cut_end)*int(fps)

    initialized = False
    frame_count = 0
    while True:

        ret, frame = cap.read()
        if not ret:
            print("exiting")
            break
        if not initialized:
            out = cv.VideoWriter("cut_video.avi", fourcc, fps, (frame.shape[1],frame.shape[0]))
            initialized = True

        if frame_count in range(start,end):
            out.write(frame)
        frame_count += 1

    cap.release()
    out.release()
    cv.destroyAllWindows()

#begin end m s ms fps parametric olarak al
# dosya input output girdi olarak hepsini fonksiyona al
#ms 250nin katları olacak yuvarla
