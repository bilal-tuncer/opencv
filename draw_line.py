import cv2 as cv
import numpy as np


img = np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(250,511),(255,0,255),2)
cv.rectangle(img, (100,250),(400,100),(0,0,255),3)
cv.putText(img, "TEXT", (110,230), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2 )

cv.imshow("black" , img)
cv.waitKey(0)
