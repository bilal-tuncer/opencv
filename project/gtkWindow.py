import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import cv2 as cv


class Scale(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(300, 300)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        #adjustment = Gtk.Adjustment(0, 0, 0.30, 1, 10, 0)

        self.scale = Gtk.Scale().new_with_range(orientation=Gtk.Orientation.HORIZONTAL,min =0.0,max = 0.30, step=0.01)
        self.scale.set_value_pos(Gtk.PositionType.TOP)
        self.scale.set_size_request(300,60)
        #self.scale.set_vexpand_set(60)
        
        #self.scale.set_hexpand(True)
        grid.attach(self.scale, 0, 0, 2, 1)

        buttonS = Gtk.Button(label="Start")
        buttonS.connect("clicked", self.start_button)
        #buttonS.set_size_request(40,30)
        grid.attach(buttonS, 0, 1, 1, 1)

        buttonF = Gtk.Button(label="Finish")
        buttonF.connect("clicked", self.finish_button)
        #buttonF.set_size_request(150,30)
        grid.attach(buttonF, 1, 1, 2, 1)

        buttonCut = Gtk.Button(label="Cut")
        buttonCut.connect("clicked", self.cut_vid)
        buttonCut.set_size_request(300,30)
        grid.attach(buttonCut, 0, 2, 2, 1)
    '''
        radiobuttonVertical = Gtk.RadioButton(group=None, label="Vertical Scale")
        radiobuttonVertical.orientation = 0
        radiobuttonVertical.connect("toggled", self.on_orientation_clicked)
        grid.attach(radiobuttonVertical, 0, 3, 2, 1)

        radiobuttonHorizontal = Gtk.RadioButton(group=radiobuttonVertical, label="Horizontal Scale")
        radiobuttonHorizontal.orientation = 1
        radiobuttonHorizontal.connect("toggled", self.on_orientation_clicked)
        grid.attach(radiobuttonHorizontal, 0, 4, 2, 1)


        self.frame = Gtk.Frame()
        Image = cv.imread("images/reduced.jpg")
        self.frame.add(Image)
        grid.attach(self.frame,0,3,2,1)
    '''      


    def start_button(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.BOTTOM, "Start")

    def finish_button(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.BOTTOM, "Finish")

    def cut_vid(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.TOP, "Cut")
    '''
    def on_orientation_clicked(self, radiobutton):
        if radiobutton.orientation == 0:
            self.scale.set_orientation(Gtk.Orientation.VERTICAL)
        else:
            self.scale.set_orientation(Gtk.Orientation.HORIZONTAL)
    '''
window = Scale()
window.show_all()
print("AAAAAAAA")

Gtk.main()
print("BBBBB")