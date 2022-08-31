import cv2 as cv
import gi
import numpy as np

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GdkPixbuf

img_flag = False
cutInterval = None
gl_size = None
gl_fps = None
gl_fourcc = 'XVID'


class File(Gtk.Window):
    in_fp = None
    out_fp = None

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(300, 120)
        self.connect("destroy", close)
        
        self.grid = Gtk.Grid()
        self.grid.set_border_width(50)
        self.grid.set_row_spacing(10)
        self.add(self.grid)

        label = Gtk.Label(label="Input File")
        self.grid.attach(label,0,0,2,1)

        self.in_filechooserbutton = Gtk.FileChooserButton(title="Select a file")
        self.in_filechooserbutton.set_filename("sample.mp4")
        self.in_filechooserbutton.set_size_request(200,30)
        self.in_filechooserbutton.connect("file-set", self.in_file_changed)
        self.grid.attach(self.in_filechooserbutton,0,1,2,1)

        label = Gtk.Label(label="")
        self.grid.attach(label,0,2,2,1)

        button = Gtk.Button(label="Save")
        button.connect("clicked",self.save)
        self.grid.attach(button,0,4,2,1)

        self.spinner = Gtk.Spinner()


    def in_file_changed(self,in_filechooserbutton):
        print("Input file selected: %s" % in_filechooserbutton.get_filename())

    def out_file_changed(self,out_filechooserbutton):
        print("Output file selected: %s" % out_filechooserbutton.get_filename())

    def save(self,button):
        self.in_fp = self.in_filechooserbutton.get_filename()
        self.remove(self.grid)
        self.add(self.spinner)
        self.spinner.start()
        self.show_all()
        #self.out_fp = self.out_filechooserbutton.get_filename()
        Gtk.main_quit(self)
        self.hide()


class Scale(Gtk.Window):
    strt = None
    finsh = None
    cropPoints = []
    frame_orgsize = None
    frame_small = None
    out_file = None
    def __init__(self,in_fp,video_time,org_fps):
        Gtk.Window.__init__(self)
        self.set_default_size(375, 700)
        self.connect("destroy", close)
        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow)
        
        self.frames = self.read_video(in_fp)
        self.clean = np.zeros((self.frame_orgsize[1],self.frame_orgsize[0],3),dtype= np.uint8)
        self.layer = self.clean.copy()
        self.is_clean = True
        self.is_changed = False
        self.frame_small = self.rescale()

        grid = Gtk.Grid()
        grid.set_border_width(10)
        grid.set_row_spacing(3)
        grid.set_column_spacing(1)

        scrolledwindow.add(grid)
        self.org_fps = org_fps
        label1 = Gtk.Label(label="Chose an interval to clip")
        grid.attach(label1,0,1,2,1)

        self.scale = Gtk.Scale().new_with_range(orientation=Gtk.Orientation.HORIZONTAL,min =0.0,max = video_time, step=0.1)
        self.scale.set_size_request(300,20)
        self.scale.set_draw_value(False)
        self.scale.connect("value-changed", self.reframe)
        grid.attach(self.scale, 0, 2, 2, 1)

        self.label = Gtk.Label(label=seconds_to_m_s_ms(0))
        grid.attach(self.label,0,3,2,1)

        buttonS = Gtk.Button(label="Start")
        buttonS.connect("clicked", self.start_button)
        grid.attach(buttonS, 0, 4, 1, 1)

        buttonF = Gtk.Button(label="Finish")
        buttonF.connect("clicked", self.finish_button)
        buttonF.set_size_request(147,30)
        grid.attach(buttonF, 1, 4, 2, 1)

        buttonClear = Gtk.Button(label="Clear")
        buttonClear.connect("clicked", self.clear_choice)
        grid.attach(buttonClear, 0, 5, 2, 1)

        buttonCut = Gtk.Button(label="Cut")
        buttonCut.connect("clicked", self.cut_vid)
        buttonCut.set_size_request(300,30)
        grid.attach(buttonCut, 0, 6, 2, 1)

        label = Gtk.Label(label="")
        label.set_size_request(300,5)
        grid.attach(label,0,7,2,1)

        label = Gtk.Label(label="Choose an area to crop")
        label.set_size_request(300,30)
        grid.attach(label,0,8,2,1)

        self.togglebutton = Gtk.ToggleButton(label="Crop:Passive")
        self.togglebutton.set_size_request(150,30)
        self.togglebutton.connect("clicked",self.croptoggled)
        grid.attach(self.togglebutton,0,9,1,1)
        
        clbutton = Gtk.Button(label="Clear Area")
        clbutton.connect("clicked",self.clpoints)
        grid.attach(clbutton,1,9,1,1)

        label2 = Gtk.Label(label="Enter size")
        label2.set_size_request(300,30)
        grid.attach(label2,0,10,2,1)

        self.width_entry = Gtk.Entry()
        self.width_entry.set_placeholder_text("Enter 'Width'")
        self.width_entry.set_size_request(150,30)
        grid.attach(self.width_entry, 0, 11, 1, 1)

        self.height_entry = Gtk.Entry()
        self.height_entry.set_placeholder_text("Enter 'Height'")
        self.height_entry.set_size_request(150,30)
        grid.attach(self.height_entry, 1, 11, 1, 1)

        button_size = Gtk.Button(label="Add")
        button_size.connect("clicked", self.save_size)
        grid.attach(button_size, 0, 12, 2, 1)

        label3 = Gtk.Label(label="")
        label3.set_size_request(300,10)
        grid.attach(label3,0,13,2,1)

        label = Gtk.Label(label="FPS :")
        grid.attach(label,0,14,1,1)

        self.fps_entry = Gtk.Entry()
        self.fps_entry.set_placeholder_text("{}".format(org_fps))
        grid.attach(self.fps_entry,1,14,1,1)

        label = Gtk.Label(label="FOURCC :")
        grid.attach(label,0,15,1,1)

        self.fourcc_entry = Gtk.Entry()
        self.fourcc_entry.set_placeholder_text("XVID")
        grid.attach(self.fourcc_entry,1,15,1,1)

        label3 = Gtk.Label(label="")
        label3.set_size_request(300,10)
        grid.attach(label3,0,16,2,1)

        save_button = Gtk.Button(label="Save Changes")
        save_button.connect("clicked", self.saveAll)
        save_button.set_size_request(250,30)
        grid.attach(save_button, 0,17,2,1)

        self.frame = Gtk.Frame()
        self.frame.set_size_request(self.frame_small[0],self.frame_small[1])
        self.reframe(None)
        
        eventbox = Gtk.EventBox()
        eventbox.set_size_request(self.frame_small[0],self.frame_small[1])
        eventbox.connect("button-press-event",self.chosen_point)
        eventbox.connect("button-release-event",self.break_point)
        eventbox.connect("event", self.event)
        eventbox.add(self.frame)
        grid.attach(eventbox,0,0,2,1)


    def rescale(self):
        a = 335/self.frame_orgsize[0]
        new_h = int(a*self.frame_orgsize[1])
        return [335,new_h]

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
        if not self.cropPoints:
            self.cropPoints = None
        Gtk.main_quit()

    def read_video(self,in_fp):
        cap = cv.VideoCapture(in_fp)
        if not cap.isOpened():
            print("Cannot open")
            exit()
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                print("read")
                break
            frames.append(frame)
        self.frame_orgsize = [frames[0].shape[1],frames[0].shape[0]]
        return frames

    def reframe(self,scale):
        value = self.scale.get_value()
        self.label.set_label(seconds_to_m_s_ms(value))
        pic = self.frames[seconds_to_frame(value,self.org_fps)]
        if not self.is_clean:
            gray = cv.cvtColor(self.layer,cv.COLOR_BGR2GRAY)
            mask = cv.inRange(gray,10,255)
            in_pic = cv.bitwise_and(pic,pic,mask=mask)
            mask = cv.bitwise_not(mask)
            pic = cv.cvtColor(pic,cv.COLOR_BGR2HSV)
            dark = np.zeros(pic.shape,pic.dtype)
            dark[:,:] = [0,0,70]
            pic = cv.subtract(pic,dark)
            pic = cv.blur(pic,ksize=(9,9))
            pic = cv.cvtColor(pic,cv.COLOR_HSV2BGR)
            masked_pic = cv.bitwise_and(pic,pic,mask=mask)
            pic = cv.add(masked_pic,in_pic)
        pic_xsize = self.frame_small[0]
        pic_ysize = self.frame_small[1]
        pic = cv.resize(pic, (pic_xsize,pic_ysize))
        pic = cv.cvtColor(pic,cv.COLOR_BGR2RGB)
        pic = np.array(pic).ravel()
        pixbuf = GdkPixbuf.Pixbuf.new_from_data(pic,GdkPixbuf.Colorspace.RGB, False, 8, pic_xsize, pic_ysize, 3*pic_xsize)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        global img_flag
        if img_flag == True:
            self.frame.remove(self.Image)
        else:
            img_flag = True
        self.Image = image
        self.frame.add(self.Image)
        self.frame.show_all()


    def chosen_point(self,widget,key):
        if self.togglebutton.get_active():
            chosen = [self.frame.get_pointer()[0],self.frame.get_pointer()[1]]
            if chosen[1] > self.frame_small[1] or chosen[0] > self.frame_small[0] or chosen[0]<0 or chosen[1]<0:
                print("Choose a point inside the picture !")
            else:    
                point = pts_of_orgsize(self.frame_orgsize,self.frame_small,chosen)
                if len(self.cropPoints) < 1:
                    self.is_clean = False
                    self.is_changed = True
                    self.cropPoints.append(point)


    def event(self,widget,key):
        if len(self.cropPoints) > 0:
            if self.togglebutton.get_active():
                chosen = [self.frame.get_pointer()[0],self.frame.get_pointer()[1]]
                if chosen[1] > self.frame_small[1] or chosen[0] > self.frame_small[0] or chosen[0]<0 or chosen[1]<0:
                    print("Choose a point inside the picture !")
                else:    
                    point = pts_of_orgsize(self.frame_orgsize,self.frame_small,chosen)
                    if len(self.cropPoints) == 2:
                        self.cropPoints.pop()
                    self.cropPoints.append(point)
                    self.layer = self.clean.copy()
                    cv.rectangle(self.layer,self.cropPoints[0],self.cropPoints[1],(0,255,0),-1)
                    
                    self.reframe(None)
                    
    def break_point(self,widget,key):
        if self.togglebutton.get_active():
            self.togglebutton.set_active(False)
            self.togglebutton.set_label("Crop:Passive")
            self.show_all()

    def croptoggled(self,button):
        if button.get_active():
            button.set_active(True)
            button.set_label("Crop:Active")
            self.is_clean = False
            self.reframe(None)
        else:
            button.set_active(False)
            button.set_label("Crop:Passive")
            if not self.is_changed:
                self.is_clean = True
                self.reframe(None)

    def clpoints(self,button):
        self.cropPoints.clear()
        self.layer = self.clean.copy()
        self.is_changed = False
        self.is_clean = True
        self.reframe(None)

def close(window):
        print("Program terminated")
        exit()

def pts_of_orgsize(org,temp,pt):
    org_pt = []
    org_pt.append(int(org[0]/temp[0] * pt[0]))
    org_pt.append(int(org[1]/temp[1] * pt[1]))
    return org_pt

def add_pt_to_frames(point,frames):
    for i in frames:
        cv.circle(i,point,2,(0,0,255),2)

def add_rect_to_frames(points,frames):
    for i in frames:
        cv.rectangle(i,points[0],points[1],(0,255,0),2)

def editVideo(out_fp):

    filewin = File()
    filewin.show_all()
    Gtk.main()

        
    in_fp = filewin.in_fp
    #out_fp = filewin.out_fp

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
    fps = gl_fps
    fourccode = gl_fourcc
    if fps == None:
        fps = org_fps
    fps = int(fps)
    fourcc = cv.VideoWriter_fourcc(*fourccode)

    cutTS = cutInterval
    size = gl_size
    if cutTS != None:
        start = seconds_to_frame(cutTS[0],org_fps)
        end = seconds_to_frame(cutTS[1],org_fps)
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
            out = cv.VideoWriter(out_fp, fourcc, fps, size)
            initialized = True

        out.write(editted)

def calc_time(fps,frame_number):
    seconds = frame_number/fps
    return seconds

def seconds_to_m_s_ms(s):
    m = int(s/60)
    ms = int((s%1)*1000)
    s = int(s)
    s = s%60
    return "{}m {}s {}ms".format(m,s,ms)

def seconds_to_frame(s,fps):
    quarter = int((s%1)*4)
    s = int(s)
    return s*int(fps)+int(fps*(quarter/4))

def cropIMG(img,top_left,bottom_right):
    cropped = img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0],:]
    return cropped

if __name__ == "__main__":
    input_path = "sample.mp4"
    output_path = "out_video.avi"

    editVideo(output_path)