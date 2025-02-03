# https://sparkle-mdm.medium.com/python-computer-vision-tutorials-image-fourier-transform-part-3-e65d10be4492

import numpy as np
import cv2

img_path = 'images/parrot.jpeg'
img = cv2.imread(img_path)[:,:,0] # gray-scale image
w,h = img.shape
side = min(w,h)
img = img[:side, :side] # crop to 700 x 700 

r = 50 # how narrower the window is
ham = np.hamming(side)[:,None] # 1D hamming
ham2d = np.sqrt(np.dot(ham, ham.T)) ** r # expand to 2D hamming
# For high-pass
#ham2d = np.ones((side,side)) - ham2d

f = cv2.dft(img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
f_shifted = np.fft.fftshift(f)
f_complex = f_shifted[:,:,0]*1j + f_shifted[:,:,1]
f_filtered = ham2d * f_complex

f_filtered_shifted = np.fft.fftshift(f_filtered)
inv_img = np.fft.ifft2(f_filtered_shifted) # inverse F.T.
filtered_img = np.abs(inv_img)
filtered_img -= filtered_img.min()
filtered_img = filtered_img*255 / filtered_img.max()
filtered_img = filtered_img.astype(np.uint8)

np_hz1  = np.hstack((img/255.0, f_shifted[:,:,1]))
np_hz2  = np.hstack((ham2d, filtered_img/255.0))
np_hz   = np.hstack((np_hz1, np_hz2))

cv2.imshow('Low-pass filtering',np_hz)

cv2.waitKey(0)
cv2.destroyAllWindows()
