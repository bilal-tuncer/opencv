import cv2 as cv
import time
import base64

class webcam:
    def __init__(self):
        self.startflag = 0
        self.threshold = 127
    
    def process(self):
        while self.startflag:
            ret, frame = self.cap.read()
            if not ret:
                self.startflag = 0
                break
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    def streambyte(self):
        while self.startflag:
            ret, frame = self.cap.read()
            if not ret:
                self.startflag = 0
                break
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield(base64.b64encode(frame))

    def start(self):
        self.cap = cv.VideoCapture(0)
        self.startflag = 1
    
    def stop(self):
        self.startflag = 0
        self.cap.release()
    
    def start_with_delay(self,delay):
        time.sleep(delay)
        self.start()

    def is_running(self):
        if self.startflag == 0:
            return("NOT RUNNING")
        else:
            return("RUNNING")

    def config(self,threshold):
        self.threshold = threshold
        return{"Threshold" : threshold}

    def status(self):
        return{"Stream" : self.is_running(), "Threshold" : self.threshold}
        
            
    


        