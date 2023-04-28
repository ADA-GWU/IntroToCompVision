import numpy as np
import cv2 as cv
from skimage.morphology import square, binary_closing, binary_opening

img = cv.imread('images/flower.png', cv.IMREAD_GRAYSCALE)


thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw/255

img_close = binary_closing(im_bw,square(4))
img_open = binary_opening(img_close,square(3))

np_hz  = np.hstack((im_bw, img_close))
np_hz1 = np.hstack((np_hz, img_open))

cv.imshow('Original, Closing and Opening',np_hz1)

cv.waitKey(0) 
cv.destroyAllWindows() 

