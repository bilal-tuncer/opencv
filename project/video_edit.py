import cv2 as cv
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

def editVideo(in_fp, out_fp, cutTS = None, cropPoints = None, size = None, fps= None, fourccode='XVID'):

    cap = cv.VideoCapture(in_fp)
    if not cap.isOpened():
        print("Cannot open")
        exit()
    
    org_fps = cap.get(cv.CAP_PROP_FPS)
    frame_number = cap.get(cv.CAP_PROP_FRAME_COUNT)
    if fps == None:
        fps = org_fps
    
    fourcc = cv.VideoWriter_fourcc(*fourccode)

    if cutTS != None:
        start = minutes_to_frame(cutTS[0],org_fps)
        end = minutes_to_frame(cutTS[1],org_fps)
        if start > end or end > frame_number:
            print("ERROR: Time steps is not compatible with {} file".format(in_fp))
            exit()

    initialized = False
    frame_count = 0
    while True:

        ret, frame = cap.read()
        if not ret:
            print("exiting")
            break
        frame_count += 1
        if not initialized:
            if cropPoints != None:
                bottom_right = cropPoints[1]
                top_left = cropPoints[0]
                w = bottom_right[0] - top_left[0]
                h = bottom_right[1] - top_left[1]
                if w > frame.shape[1] or h > frame.shape[0]:
                    print("ERROR: Size is not compatible with {} file".format(in_fp))
                    exit()
        if cutTS != None:
            if frame_count < start:
                continue
            elif frame_count > end:
                break
        editted = frame
        if cropPoints != None:
            editted = cropIMG(frame,top_left,bottom_right)

        if size != None:
            editted = cv.resize(editted,size)
        
        if not initialized:
            size[0] = editted.shape[1]
            size[1] = editted.shape[0]
            out = cv.VideoWriter(out_fp, fourcc, fps, size)
            initialized = True

        out.write(editted)


def minutes_to_frame(m,fps):
    s = ((100*m) % (100))
    quarter = int((s%1)*4)
    s = int(s)  
    m = int(m)
    return (m*60 + s)*int(fps)+int(fps*(quarter/4))

def cropIMG(img,top_left,bottom_right):
    cropped = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    return cropped

if __name__ == "__main__":
    input_path = "sample.mp4"
    output_path = "out_video.avi"

    editVideo(input_path,output_path,cropPoints= [[150,150],[400,400]],cutTS=[0.15,0.30], size=[600,600], fps=30)