import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

im = cv2.imread('images/balloon.png')
img = rgb2gray(im)

s = np.linspace(0, 2*np.pi, 400)
r = 370 + 320*np.sin(s)
c = 440 + 320*np.cos(s)

init = np.array([r, c]).T

snake = active_contour(img, init, alpha=0.5, beta=0.01, w_line=-5, w_edge=0, gamma=0.1)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(im, cmap=plt.cm.gray)
ax.plot(init[:, 1], init[:, 0], '--b', lw=1)
ax.plot(snake[:, 1], snake[:, 0], '-r', lw=2)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])

plt.show()
