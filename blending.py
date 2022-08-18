import cv2 as cv
import numpy as np

apple = cv.imread("apple.jpg")
orange = cv.imread("orange.jpg")

Gapple = apple.copy()
Gorange = orange.copy()
pO = [Gorange]
pA = [Gapple]

for i in range(6):
    Gapple = cv.pyrDown(Gapple)
    pA.append(Gapple)
    Gorange = cv.pyrDown(Gorange)
    pO.append(Gorange)

lpA = [pA[5]]
lpO = [pO[5]]
for i in range(5,0,-1):
    newGa = cv.pyrUp(pA[i])
    La = cv.subtract(pA[i-1],newGa)
    lpA.append(La)
    newGo = cv.pyrUp(pO[i])
    Lo = cv.subtract(pO[i-1],newGo)
    lpO.append(Lo)


LS = []
for la,lb in zip(lpA,lpO):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)

for i in range(6):
    cv.imshow("{}".format(i),LS[i])
cv.waitKey(0)
cv.destroyAllWindows()
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

cv.imshow("blend",ls_)
cv.waitKey(0)
