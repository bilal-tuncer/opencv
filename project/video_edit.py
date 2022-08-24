import cv2 as cv
import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

cutInterval = None
gl_size = None
gl_fps = None
gl_fourcc = 'XVID'

class Scale(Gtk.Window):
    strt = None
    finsh = None
    def __init__(self,video_time,org_fps):
        Gtk.Window.__init__(self)
        self.set_default_size(300, 300)
        self.connect("destroy", self.close)

        grid = Gtk.Grid()
        grid.set_border_width(10)
        grid.set_row_spacing(3)
        grid.set_column_spacing(1)

        self.add(grid)

        label1 = Gtk.Label(label="Chose an interval to cut the video")
        grid.attach(label1,0,0,2,1)

        self.scale = Gtk.Scale().new_with_range(orientation=Gtk.Orientation.HORIZONTAL,min =0.0,max = video_time, step=0.01)
        self.scale.set_value_pos(Gtk.PositionType.TOP)
        self.scale.set_size_request(300,60)
        grid.attach(self.scale, 0, 1, 2, 1)

        buttonS = Gtk.Button(label="Start")
        buttonS.connect("clicked", self.start_button)
        grid.attach(buttonS, 0, 2, 1, 1)

        buttonF = Gtk.Button(label="Finish")
        buttonF.connect("clicked", self.finish_button)
        buttonF.set_size_request(147,30)
        grid.attach(buttonF, 1, 2, 2, 1)

        buttonClear = Gtk.Button(label="Clear")
        buttonClear.connect("clicked", self.clear_choice)
        grid.attach(buttonClear, 0, 3, 2, 1)

        buttonCut = Gtk.Button(label="Cut")
        buttonCut.connect("clicked", self.cut_vid)
        buttonCut.set_size_request(300,30)
        grid.attach(buttonCut, 0, 4, 2, 1)

        label2 = Gtk.Label(label="Enter size")
        label2.set_size_request(300,30)
        grid.attach(label2,0,5,2,1)

        self.width_entry = Gtk.Entry()
        self.width_entry.set_placeholder_text("Enter 'Width'")
        self.width_entry.set_size_request(150,30)
        grid.attach(self.width_entry, 0, 6, 1, 1)

        self.height_entry = Gtk.Entry()
        self.height_entry.set_placeholder_text("Enter 'Height'")
        self.height_entry.set_size_request(150,30)
        grid.attach(self.height_entry, 1, 6, 1, 1)

        button_size = Gtk.Button(label="Add")
        button_size.connect("clicked", self.save_size)
        grid.attach(button_size, 0, 7, 2, 1)

        label3 = Gtk.Label(label="")
        label3.set_size_request(300,10)
        grid.attach(label3,0,8,2,1)

        label = Gtk.Label(label="FPS :")
        grid.attach(label,0,9,1,1)

        self.fps_entry = Gtk.Entry()
        self.fps_entry.set_placeholder_text("{}".format(org_fps))
        grid.attach(self.fps_entry,1,9,1,1)

        label = Gtk.Label(label="FOURCC :")
        grid.attach(label,0,10,1,1)

        self.fourcc_entry = Gtk.Entry()
        self.fourcc_entry.set_placeholder_text("XVID")
        grid.attach(self.fourcc_entry,1,10,1,1)

        label3 = Gtk.Label(label="")
        label3.set_size_request(300,10)
        grid.attach(label3,0,11,2,1)

        save_button = Gtk.Button(label="Save Changes")
        save_button.connect("clicked", self.saveAll)
        save_button.set_size_request(250,30)
        grid.attach(save_button, 0,12,2,1)



    def close(self, window):
        print("Program ended")
        exit()

    def start_button(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.BOTTOM, "Start")
        self.strt = value
        print("Start: {}".format(value))

    def finish_button(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.BOTTOM, "Finish")
        self.finsh = value
        print("Finish: {}".format(value))

    def clear_choice(self, button):
        self.scale.clear_marks()

    def cut_vid(self, button):
        global cutInterval
        cutInterval = [self.strt,self.finsh]

    def save_size(self, button):
        global gl_size
        w = int(self.width_entry.get_text())
        h = int(self.height_entry.get_text())
        gl_size = [w,h]

    def saveAll(self,button):
        fourcc = self.fourcc_entry.get_text()
        fps = self.fps_entry.get_text()
        global gl_fps
        global gl_fourcc
        if fps:
            gl_fps = fps
        if fourcc:
            gl_fourcc = fourcc
        Gtk.main_quit()

def editVideo(in_fp, out_fp, cropPoints = None):

    cap = cv.VideoCapture(in_fp)
    if not cap.isOpened():
        print("Cannot open")
        exit()
    
    org_fps = cap.get(cv.CAP_PROP_FPS)
    frame_number = cap.get(cv.CAP_PROP_FRAME_COUNT)

    video_time = calc_time(org_fps,frame_number)

    window = Scale(video_time,org_fps)
    window.show_all()
    Gtk.main()

    fps = gl_fps
    fourccode = gl_fourcc
    if fps == None:
        fps = org_fps
    fps = int(fps)
    fourcc = cv.VideoWriter_fourcc(*fourccode)

    cutTS = cutInterval
    size = gl_size
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
            size = [editted.shape[1],editted.shape[0]]
            #size[0] = editted.shape[1]
            #size[1] = editted.shape[0]
            out = cv.VideoWriter(out_fp, fourcc, fps, size)
            initialized = True

        out.write(editted)

def calc_time(fps,frame_number):
    seconds = frame_number/fps
    minutes = int(seconds/60)
    fraction = seconds%60 / 100
    print(minutes+fraction)
    return minutes+fraction

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

    editVideo(input_path,output_path,cropPoints= [[150,150],[400,400]])