import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

global old_img
pts = []
global cnt

def choose_pt(event,x,y,flag,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global cnt
        if cnt < 4:
            global old_img
            old_img.append(img.copy())
            cv.circle(img,(x,y),1,(0,0,255),2)
            pts.append([x,y])
            print(x,y)
            cnt += 1


if __name__ == "__main__":

    path_img = "sudoku_paper.jpg"
    W = 600
    H = 600
    img = cv.imread(path_img)
    rows, cols , ch= img.shape
    cnt = 0

    img = cv.resize(img, (W,H))
    cv.namedWindow("image")
    cv.setMouseCallback("image",choose_pt)
    img_cl = img.copy()
    old_img = []
    while True:
        cv.imshow("image",img)
        if cnt > 4:
            break
        #print("count: {}".format(cnt))
        k = cv.waitKey(10)
        if k == 8:
            img = old_img.pop()
            pts.pop()
            cnt -= 1

        if k == 13:
            break
    cv.destroyAllWindows()

    arr_pts = np.float32(pts)
    dst_pts = np.float32([[0,0],[W,0],[W,H],[0,H]])
    print(arr_pts)

    M = cv.getPerspectiveTransform(arr_pts,dst_pts)
    dst = cv.warpPerspective(img_cl,M, (W,H))

    cv.imshow("final",dst)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("sudoku.jpg",dst)
    cv.destroyAllWindows()
