import cv2 as cv
import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt

img = cv.imread('images/rose.jpeg')
h,w,c = img.shape

T1 = np.array([[0.8, 0.0],
              [0.0, 0.4]])
T2 = np.array([[cos(pi/4.0),  sin(pi/4.0)],
              [sin(pi/4.0), -cos(pi/4.0)]])

T = np.matmul(T2,T1)
print('Transformation matrix:')
print(T)
print('With additional column:')
T = np.hstack((T,np.zeros((2,1))))
print(T)


dst = cv.warpAffine(img,T,(w,h))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
