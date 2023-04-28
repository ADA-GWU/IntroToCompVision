import numpy as np
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('images/wood.jpeg')
#im = cv2.imread('/Users/jhasanov/Desktop/MRI_brain.png')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# kernel size
k = 30

kernel1 = cv2.getGaborKernel(ksize=(k, k), sigma=3, theta=1*np.pi/4, lambd=1*np.pi/4, gamma=0.5, psi=0, ktype=cv2.CV_32F)
fimg1 = cv2.filter2D(img, cv2.CV_8UC3, kernel1)

kernel2 = cv2.getGaborKernel((k, k), sigma=3, theta=2*np.pi/4, lambd=1*np.pi/4, gamma=0.5, psi=0, ktype=cv2.CV_32F)
fimg2 = cv2.filter2D(img, cv2.CV_8UC3, kernel2)

kernel3 = cv2.getGaborKernel((k, k), sigma=3, theta=3*np.pi/4, lambd=1*np.pi/4, gamma=0.5, psi=0, ktype=cv2.CV_32F)
fimg3 = cv2.filter2D(img, cv2.CV_8UC3, kernel3)

kernel4 = cv2.getGaborKernel((k, k), sigma=3, theta=4*np.pi/4, lambd=1*np.pi/4, gamma=0.5, psi=0, ktype=cv2.CV_32F)
fimg4 = cv2.filter2D(img, cv2.CV_8UC3, kernel4)

fig, ax = plt.subplots(ncols=5, nrows=2, figsize=(13, 7))

ax[0][0].imshow(im)
ax[0][0].set_title('Original')
ax[1][0].imshow(img,cmap='gray')
ax[1][0].set_title('gray')

ax[0][1].imshow(kernel1)
ax[0][1].set_title('Kernel ('+str(k)+') /')
ax[1][1].imshow(fimg1,cmap='gray')
ax[1][1].set_title('Filtered')

ax[0][2].imshow(kernel2)
ax[0][2].set_title('Kernel ('+str(k)+') -')
ax[1][2].imshow(fimg2,cmap='gray')
ax[1][2].set_title('Filtered')

ax[0][3].imshow(kernel3)
ax[0][3].set_title('Kernel ('+str(k)+') \\')
ax[1][3].imshow(fimg3,cmap='gray')
ax[1][3].set_title('Filtered')

ax[0][4].imshow(kernel4)
ax[0][4].set_title('Kernel ('+str(k)+') |')
ax[1][4].imshow(fimg4,cmap='gray')
ax[1][4].set_title('Filtered')


plt.show()

