import cv2 as cv
import numpy as np
import os 

for root, dirs, files in os.walk("/home/bil/Documents/Rakamlar"):
    for file in files:
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            print(path)
            img = cv.imread(path)
            h ,w ,ch = img.shape
            img = cv.GaussianBlur(img,(5,5),2)

            lower_bound = np.array([65,65,65])
            upper_bound = np.array([255,255,255])
            #hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
            hsv = img
            mask = cv.inRange(hsv , lower_bound, upper_bound)  
            mask = cv.bitwise_not(mask)

            nimg = cv.bitwise_and(img,img,mask=mask)
            minimg = cv.resize(nimg,[int(w/8),int(h/8)])
            cv.imshow("img",minimg)
            k = cv.waitKey(0)
            if k == 27:
                exit()
            if k == ord("w"):           #write
                cv.imwrite(path,mask)