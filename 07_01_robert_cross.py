import numpy as np
import cv2 as cv
from scipy import ndimage
 
fname = 'images/coins.png'
#fname = 'helicopter.jpeg'

img_color = cv.imread(fname)

img = cv.imread(fname, cv.IMREAD_GRAYSCALE)

thresh = 127
im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
im_bw = im_bw/255

 
roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )
  
vertical = ndimage.convolve( im_bw, roberts_cross_v )
horizontal = ndimage.convolve( im_bw, roberts_cross_h )
  
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255

np_hz1  = np.hstack((img/255, vertical))
np_hz2  = np.hstack((horizontal, edged_img))
np_vz = np.vstack((np_hz1, np_hz2))

cv.imshow('Original',img_color)
cv.waitKey(0) 

cv.imshow('2 Grayscales, B&W and Robert Cross',np_vz)

cv.waitKey(0) 
cv.destroyAllWindows() 

