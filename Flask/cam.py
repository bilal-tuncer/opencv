from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response
import cv2 as cv


app = Flask(__name__)
cap = cv.VideoCapture(0)
@app.route('/<name1>/')
def home_page(name1):
   return render_template("index.html",name = name1)
#app.add_url_rule("/", "home", home_page)

@app.route("/")
def root():
   #return redirect(url_for("home_page",name1 = "nameless"))
   return redirect(url_for("home_page",name1 = "nameless"))

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen():  
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
if __name__ == '__main__':
   app.run(host="0.0.0.0",port="8080")

