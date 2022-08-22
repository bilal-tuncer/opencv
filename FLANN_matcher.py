import cv2 as cv
import numpy as np

logo = cv.imread("adidas.jpg",0)            #query
tshirt = cv.imread("adidas_tshirt.jpg",0)   #train

logo = cv.pyrDown(logo)

sift = cv.SIFT_create()

kp1, des1 = sift.detectAndCompute(logo,None)
kp2, des2 = sift.detectAndCompute(tshirt,None)

#FLANN parameters 
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.6*n.distance:
        matchesMask[i]=[1,0]

draw_params = dict(matchColor = (0,255,0),          #good matches will be green
                   singlePointColor = (255,0,0),    #bad matches or single points will bi red
                   matchesMask = matchesMask,
                   flags = cv.DrawMatchesFlags_DEFAULT)
img3 = cv.drawMatchesKnn(logo,kp1,tshirt,kp2,matches,None,**draw_params)

cv.imshow(" ",img3)
cv.waitKey(0)