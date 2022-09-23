import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


logo = cv.imread("adidas.jpg",0)            #query
tshirt = cv.imread("adidas_tshirt.jpg",0)   #train

logo = cv.pyrDown(logo)

SIFT = cv.SIFT_create()
kp1, des1 = SIFT.detectAndCompute(logo,None)
kp2,des2 = SIFT.detectAndCompute(tshirt,None)

f_logo = cv.drawKeypoints(logo,kp1,None)
f_tshirt = cv.drawKeypoints(tshirt,kp2,None)


bf = cv.BFMatcher(crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 40 matches.
img3 = cv.drawMatches(logo,kp1,tshirt,kp2,matches[:40],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.imshow("",img3)

#knn matches

bf2 = cv.BFMatcher()

#it returns 2 matches for a keypoint. first one is the best match,
# second one is used to check the best one is a good match. 
matches = bf2.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.7*n.distance: # check if there is a similar match
        good.append([m])
img3 = cv.drawMatchesKnn(logo,kp1,tshirt,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow("knn",img3)
cv.waitKey(0)
cv.destroyAllWindows()
