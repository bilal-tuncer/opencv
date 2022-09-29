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
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    
    initialized = False
    while True:

        ret, frame = cap.read()
        if not ret:
            print("exiting")
            break
        if not initialized:
            out = cv.VideoWriter("compressed.avi", fourcc, fps, (frame.shape[1],frame.shape[0]))
        initialized = True
        cv.imwrite("images/template.jpg",frame)
        img = Image.open("images/template.jpg")
        img.save("images/reduced.jpg",quality = 50,optimize = True)

        reduced = cv.imread("images/reduced.jpg")
        out.write(reduced)

    cap.release()
    out.release()
    cv.destroyAllWindows()
