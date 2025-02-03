import numpy as np
import cv2
from matplotlib import pyplot as plt

# read two input images as grayscale images
imgL = cv2.imread('images/TsukubaR.png',0)
imgR = cv2.imread('images/TsukubaL.png',0)

# Initiate and StereoBM object
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)

# compute the disparity map
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
disparity.shape
