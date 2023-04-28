import numpy as np
import cv2 as cv
from skimage.morphology import square, erosion, dilation

img = cv.imread('images/shapes_bw.jpeg', cv.IMREAD_GRAYSCALE)
thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw / 255

img_ers = erosion(im_bw, square(3))
img_bdr = im_bw - img_ers

np_hz  = np.hstack((im_bw, img_ers))
np_hz  = np.hstack((np_hz, img_bdr))


cv.imshow('Original, Erosion and (Original-Erosion)',np_hz)

cv.waitKey(0) 
cv.destroyAllWindows() 

