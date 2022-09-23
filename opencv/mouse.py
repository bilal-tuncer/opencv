import numpy as np
import cv2 as cv

def nothing(aa):
    pass

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),50,(b,g,r),2)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(20)
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('circles.jpg' , img)

    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
cv.destroyAllWindows()
