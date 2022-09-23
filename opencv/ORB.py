#free way to find keypoints instead of SIFT and SURF

import cv2 as cv
import numpy as np

img = cv.imread("3dshapes.jpg",0)

orb = cv.ORB_create()

keypoints = orb.detect(img,None)

n_img = cv.drawKeypoints(img,keypoints,None,(255,0,0))

cv.imshow("kp",n_img)
cv.waitKey(0)
cv.destroyAllWindows()