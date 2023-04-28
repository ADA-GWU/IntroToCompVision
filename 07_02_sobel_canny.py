import numpy as np
import cv2

# Read the original image
img = cv2.imread('images/bigwheelbike.jpeg') 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img, (7,7), 0) 

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_16S, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)


# Canny Edge Detection
canny_edges = cv2.Canny(image=img_blur, threshold1=50, threshold2=150) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', canny_edges)

np_hz1  = np.hstack((img/255, img_blur/255))
np_hz2  = np.hstack((sobelxy, canny_edges))
np_vz = np.vstack((np_hz1, np_hz2))

cv2.imshow('Original, Blurred, Canny, Sobel',np_vz)

cv2.waitKey(0)

cv2.destroyAllWindows()
