import cv2 as cv
import numpy as np
from flask import Response
from flask import Flask
from flask import render_template
from flask import url_for, redirect
import time

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate():
    cap = cv.VideoCapture("sample.mp4")
    while(True):
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(wait)

if __name__ == "__main__":

    cap = cv.VideoCapture("sample.mp4")
    fps = cap.get(cv.CAP_PROP_FPS)
    wait = (1/fps)

    app.run(host="0.0.0.0",port=8080,debug=True)