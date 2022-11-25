from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse, RedirectResponse
from webcam import webcam
import asyncio

app = FastAPI()
cam = webcam()

@app.get("/")
async def root():
    return {"message": "StreamAPI"}

@app.get("/start")
async def start():

    if cam.startflag == 0:
        cam.start()
        return{"message" : "started"}
    else :
        return{"message" : "already started!"}

@app.get("/startdelay/{delay}")
async def start_with_delay(delay : int):
    if cam.startflag == 0:
        cam.start_with_delay((delay))
        return{"message" : "started"}
    return{"message":"already started !"}

@app.get("/stop")
async def stop():
    if cam.startflag == 1:
        cam.stop()
        return{"message" : "stopped"}
    else :
        return{"message" : "not running!"}

@app.get("/status")
async def status():
    return cam.status()

@app.get("/config/{threshold}")
async def config(threshold : int):
    return cam.config(threshold= threshold)

@app.get("/stream")
async def stream():
    return StreamingResponse(cam.process(), media_type='multipart/x-mixed-replace; boundary=frame')

@app.get("/streambyte")
async def byte():
    return Response(cam.streambyte(), media_type= "byte")
