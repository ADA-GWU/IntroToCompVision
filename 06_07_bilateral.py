import numpy as np
import cv2 as cv

img = cv.imread('images/newspaper.jpeg')

w,h,c = img.shape

#blur1 = cv.GaussianBlur(img,(15,15),0)
blur1 = cv.bilateralFilter(img,9,75,75)


np_hz1  = np.hstack((img, np.zeros_like(img,shape=(w,5,c))))
np_hz1  = np.hstack((np_hz1, blur1))

cv.imshow('Bilateral filter',np_hz1)

cv.waitKey(0) 
cv.destroyAllWindows() 

