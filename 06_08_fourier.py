# https://docs.opencv.org/3.4/de/dbc/tutorial_py_fourier_transform.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def get_freq(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    mag_spec = abs(fshift) #np.log(np.abs(fshift))
    return mag_spec

def read_bw_img(fname):
    img = cv.imread(fname, cv.IMREAD_GRAYSCALE)
    thresh = 127
    im_bw = cv.threshold(img, thresh, 255, cv.THRESH_BINARY)[1]
    im_bw = im_bw/255
    return im_bw

img1 = read_bw_img('images/stripes_low_rot.jpeg')
img2 = read_bw_img('images/stripes_high.png')

#img = cv.imread('inchi2.png',0)

ff1 = get_freq(img1)
ff2 = get_freq(img2)

plt.subplot(221),plt.imshow(img1, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(ff1, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(ff2, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()

