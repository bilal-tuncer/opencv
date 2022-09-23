import cv2 as cv
import os

import os
'''for root, dirs, files in os.walk("/home/bil/git_code/work/Rakamlar(cutted)"):
    for file in files:
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            print(path)
            img = cv.imread(path)
            h ,w ,ch = img.shape
            #4032  3024  3
            print(h,w,ch)

            minimg = cv.resize(img,[int(w/8),int(h/8)])
            img = img[:h-500,:,:]
            h ,w ,ch = img.shape
            minimg2 = cv.resize(img,[int(w/8),int(h/8)])
            cv.imshow("img",minimg)
            cv.imshow("img_e",minimg2)
            k = cv.waitKey(0)
            if k == 27:
                exit()
            
            if k == ord("s"):
                cv.imwrite(path,img)'''


img = cv.imread("/home/bil/git_code/work/Rakamlar(cutted)/2/2_1/photo-1663833812835.jpg")

h ,w ,ch = img.shape
#4032  3024  3
print(h,w,ch)
img = img[700:,:,:]
minimg = cv.resize(img,[int(w/8),int(h/8)])

cv.imshow("img",minimg)
k = cv.waitKey(0)
if k == 27:
    exit()

cv.imwrite("/home/bil/git_code/work/Rakamlar(cutted)/2/2_1/photo-1663833812835.jpg",img)
