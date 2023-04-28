import cv2 as cv
import numpy as np

img = cv.imread('demo.jpg')
img_gr = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

h,w = img_gr.shape
print('shape',w,h)

img_gr = img_gr/255

img_gr1 = (img_gr / 0.1)
img_gr2 = (img_gr / 0.2)
img_gr3 = (img_gr / 0.5)

np_hz1  = np.hstack((img_gr, img_gr1))
np_hz2  = np.hstack((img_gr3, img_gr2))
np_vrt = np.vstack((np_hz1,np_hz2))

cv.imshow('Grayscale',np_vrt)

cv.waitKey(0) 
cv.destroyAllWindows() 
