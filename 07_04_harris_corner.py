#https://medium.com/data-breach/introduction-to-harris-corner-detector-32a88850b3f6
#https://github.com/deepanshut041/feature-detection/tree/master/harris

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read in the image
img = cv2.imread('images/shapes_bw.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = 200
gray = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
#gray = gray/255

# Detect corners 
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

plt.imshow(dst, cmap='gray')

# This value vary depending on the image and how many corners you want to detect
# Try changing this free parameter, 0.1, to be larger or smaller and see what happens
thresh = 0.1*dst.max()

# Create an image copy to draw corners on
corner_image = np.copy(gray)

# Iterate through all the corners and draw them on the image (if they pass the threshold)
for j in range(0, dst.shape[0]):
    for i in range(0, dst.shape[1]):
        if(dst[j,i] > thresh):
            # image, center pt, radius, color, thickness
            cv2.circle( corner_image, (i, j), 2, (200,0,0), 2)

plt.imshow(corner_image)
plt.show()


