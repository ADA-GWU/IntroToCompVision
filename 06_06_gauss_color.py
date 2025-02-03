import numpy as np
import cv2 as cv

img = cv.imread('images/color1.jpeg')
w,h,c = img.shape

blur1 = cv.GaussianBlur(img,(3,3),0)
blur2 = cv.GaussianBlur(img,(7,7),0)
blur3 = cv.GaussianBlur(img,(11,11),0)

np_hz1  = np.hstack((img, np.zeros_like(img,shape=(w,5,c))))
np_hz1  = np.hstack((np_hz1, blur1))

np_hz2  = np.hstack((blur2, np.zeros_like(img,shape=(w,5,c))))
np_hz2  = np.hstack((np_hz2, blur3))

w,h,c = np_hz1.shape
np_vrt  = np.vstack((np_hz1, np.zeros_like(np_hz1,shape=(5,h,c))))
np_vrt  = np.vstack((np_vrt, np_hz2))


cv.imshow('Gaussian smoothing - original, 3x3, 7x7 and 11x11 kernels',np_vrt)

cv.waitKey(0) 
cv.destroyAllWindows() 

