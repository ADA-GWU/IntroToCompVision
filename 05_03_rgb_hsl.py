import cv2 as cv
import numpy as np

img = cv.imread('demo.jpg')
img_hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)

h,w,ch = img.shape
print('shape',w,h)

# Test for data loss
back_rgb = cv.cvtColor(img_hls, cv.COLOR_HLS2BGR)
print('Data loss:',np.sum(back_rgb-img)/(w*h*ch))

# Change Hue
img_hls0 = img_hls.copy()
img_hls0[:,:,0] += 100
img_hls0[:,:,0] %= 360
img0 = cv.cvtColor(img_hls0,cv.COLOR_HLS2BGR)

# Change Lightness
img_hls1 = img_hls.copy()
img_hls1[:,:,1] += 30
img_hls1[:,:,1] = np.minimum(img_hls1[:,:,1],np.ones((h,w))*100)
img1 = cv.cvtColor(img_hls1,cv.COLOR_HLS2BGR)

# Change Saturation
img_hls2 = img_hls.copy()
img_hls2[:,:,2] +=50
img_hls2[:,:,2] = np.minimum(img_hls2[:,:,2],np.ones((h,w))*100)
img2 = cv.cvtColor(img_hls2,cv.COLOR_HLS2BGR)

np_hz1  = np.hstack((img, img0))
np_hz2  = np.hstack((img1, img2))
np_vrt = np.vstack((np_hz1,np_hz2))

cv.imshow('Clockwise: Original, Hue update, Sat update, Lightness update',np_vrt)

cv.waitKey(0) 
cv.destroyAllWindows() 
