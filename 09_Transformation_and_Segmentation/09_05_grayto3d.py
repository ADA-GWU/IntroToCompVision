import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#img = cv.imread('images/coins.png',0)
img = cv.imread('images/lena.png',0)

xx, yy = np.mgrid[0:img.shape[0], 0:img.shape[1]]

# create the figure
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xx, yy, img ,rstride=1, cstride=1, cmap=plt.cm.gray,
        linewidth=0)

# show it
plt.show()
