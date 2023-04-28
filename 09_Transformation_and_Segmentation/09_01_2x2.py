import cv2 as cv
import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt

img = cv.imread('images/rose.jpeg')
h,w,c = img.shape

# cols-1 and rows-1 are the coordinate limits.
#M = np.array([[1.0, 0.0, 0.0],
#              [0.8, 1.0, 0.0]])
M = np.array([[cos(pi/2.0),  sin(pi/2.0), 0.0],
              [sin(pi/2.0), -cos(pi/2.0), 0.0]])

print('Transformation matrix:')
print(M)

dst = cv.warpAffine(img,M,(w,h))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
