import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../images/rose.jpeg',0)
h,w = img.shape

# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((w-1)/2.0,(h-1)/2.0),127,0.7)
print('Transformation matrix:')
print(M)

dst = cv.warpAffine(img,M,(w,h))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
