import cv2 as cv
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from ui import *


def editVideo():

    filewin = inFile()
    filewin.show_all()
    Gtk.main()


    in_fp = filewin.in_fp

    cap = cv.VideoCapture(in_fp)
    if not cap.isOpened():
        print("Cannot open")
        exit()
    
    org_fps = cap.get(cv.CAP_PROP_FPS)
    frame_number = cap.get(cv.CAP_PROP_FRAME_COUNT)

    video_time = calc_time(org_fps,frame_number)

    window = Scale(in_fp,video_time,org_fps)
    window.show_all()
    Gtk.main()

    cropPoints = window.cropPoints
    fps = window.gl_fps
    fourccode = window.gl_fourcc
    if fps == None:
        fps = org_fps
    fps = int(fps)
    fourcc = cv.VideoWriter_fourcc(*fourccode)

    cutTS = window.cutInterval
    size = window.gl_size
    
    start = seconds_to_frame(cutTS[0],org_fps)
    end = seconds_to_frame(cutTS[1],org_fps)
    if start > end or end > frame_number:
        print("ERROR: Time steps is not compatible with {} file".format(in_fp))
        exit()

    outwin = outFile()
    outwin.show_all()
    Gtk.main()

    initialized = False
    frame_count = 0
    while True:

        ret, frame = cap.read()
        if not ret:
            print("Exiting")
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
            out_fp = outwin.out_fp
            size = [editted.shape[1],editted.shape[0]]
            out = cv.VideoWriter(out_fp, fourcc, fps, size)
            initialized = True

        out.write(editted)
    print("Video Saved")

def calc_time(fps,frame_number):
    seconds = frame_number/fps
    return seconds


def cropIMG(img,top_left,bottom_right):
    cropped = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    return cropped

if __name__ == "__main__":

    editVideo()
