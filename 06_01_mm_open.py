import numpy as np
import cv2 as cv
from skimage.morphology import square,binary_opening

img = cv.imread('images/inchi2.png', cv.IMREAD_GRAYSCALE)

thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw/255

custom = np.array([[0, 0, 1],
                   [0, 1, 0],
                   [1, 0, 0]], dtype=np.uint8)

img_open1 = binary_opening(im_bw,square(2))
img_open2 = binary_opening(im_bw,custom)
img_open3 = binary_opening(im_bw,square(3))

np_hz1  = np.hstack((im_bw, img_open1))
np_hz2  = np.hstack((img_open2, img_open3))
np_hz   = np.hstack((np_hz1, np_hz2))

cv.imshow('Openining - original, 2x2, custom  and 3x3 SE',np_hz)

cv.waitKey(0) 
cv.destroyAllWindows() 

