import numpy as np
import cv2 as cv
from skimage.morphology import square, binary_erosion, binary_dilation

img = cv.imread('images/inchi2.png', cv.IMREAD_GRAYSCALE)
thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw/255

img_dil = binary_dilation(im_bw, square(3))
img_ers = binary_erosion(img_dil, square(2))
img_ers2 = binary_erosion(img_ers, square(2))

np_hz1  = np.hstack((im_bw, img_dil))
np_hz2  = np.hstack((np_hz1, img_ers))
np_hz3  = np.hstack((np_hz2, img_ers2))


cv.imshow('Original, Dilation, 2 Erosions',np_hz3)

cv.waitKey(0) 
cv.destroyAllWindows() 

