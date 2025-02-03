import numpy as np
import cv2 as cv

img = cv.imread('images/inchi2.png', cv.IMREAD_GRAYSCALE)

thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw/255

img_open1 = cv.GaussianBlur(im_bw,(3,3),0)
img_open2 = cv.GaussianBlur(im_bw,(5,5),0)
img_open3 = cv.GaussianBlur(im_bw,(7,7),0)

np_hz1  = np.hstack((im_bw, img_open1))
np_hz2  = np.hstack((img_open2, img_open3))
np_hz   = np.hstack((np_hz1, np_hz2))

cv.imshow('Gaussian smoothing - original, 3x3, 5x5 and 7x7 kernels',np_hz)

cv.waitKey(0) 
cv.destroyAllWindows() 

