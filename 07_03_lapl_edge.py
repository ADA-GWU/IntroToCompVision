import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read the original image
img = cv2.imread('images/rose.jpeg') 

# Convert to graycsale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Laplacian operator in some higher datatype
laplacian1 = cv2.Laplacian(img,cv2.CV_64F)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(5,5),3)
 
# Apply Laplacian operator in some higher datatype
laplacian2 = cv2.Laplacian(blur,cv2.CV_64F)

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(laplacian1, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img, cmap = 'gray')
plt.title('Blurred'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(laplacian2, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.show()
