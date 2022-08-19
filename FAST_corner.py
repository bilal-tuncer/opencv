import cv2 as cv
import numpy as np

img = cv.imread("shapes.jpg",0)
img = cv.pyrDown(img)
img = cv.pyrDown(img)
fast = cv.FastFeatureDetector_create()
keypoints = fast.detect(img,None)
n_img = cv.drawKeypoints(img,keypoints,None,(0,255,0))

print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(keypoints)))

cv.imshow("",n_img)
cv.waitKey(0)
