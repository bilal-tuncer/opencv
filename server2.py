import asyncio
from websockets import connect
import cv2 as cv
import numpy as np
import base64
import time

async def _recv(uri):
    async with connect(uri) as websocket:
        while True:
            try:
                data = await websocket.recv()
                # print(data)
                # print(type(data))
                nparr = np.frombuffer(base64.b64decode(data), np.uint8)
                img = cv.imdecode(nparr, cv.IMREAD_COLOR)
                cv.imshow("frame" ,img)
                cv.waitKey(1)
            except:
                await asyncio.sleep(1)
                print("patladi")
                break
                


asyncio.run(_recv("ws://10.148.11.54:8080/ws"))
