import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.transform import hough_line, hough_line_peaks, hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.color import rgb2gray

# Load picture and detect edges
im = cv2.imread('images/coffee3.jpeg')
im = img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
img = rgb2gray(im)
img = img*255.0

# uncomment to see smooth edges
img = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)

# uncomment to see more edges
#edges = canny(img, sigma=3, low_threshold=5, high_threshold=20)
edges = canny(img, sigma=3, low_threshold=10, high_threshold=50)

# Detect lines
# Set a precision of 0.5 degree.
angles = np.linspace(-np.pi / 2, np.pi / 2, 360, endpoint=False)
h, theta, d = hough_line(edges, theta=angles)

angle_step = 0.5 * np.diff(theta).mean()
d_step = 0.5 * np.diff(d).mean()
bounds = [np.rad2deg(theta[0] - angle_step),
          np.rad2deg(theta[-1] + angle_step),
          d[-1] + d_step, d[0] - d_step]

# Circle detection: detect two radii
hough_radii = np.arange(20, 200, 2)
hough_res = hough_circle(edges, hough_radii)

# Maximum number of circles to find (increase to 10 to detect more)
max_circles = 23
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=max_circles)

# Draw the circles on the image
im_circle = np.copy(im)

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(13, 7))
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius,
                                    shape=im.shape)
    im_circle[circy, circx] = (255, 0, 0)

ax[0][0].imshow(edges)
ax[0][0].set_title('Edges')

ax[0][1].imshow(im_circle)
ax[0][1].set_title('Circles')

ax[1][0].imshow(np.log(1 + h), extent=bounds, aspect=1 / 10)
ax[1][0].set_title('Hough transform - lines')
ax[1][0].set_xlabel('Angles (degrees)')
ax[1][0].set_ylabel('Distance (pixels)')

ax[1][1].imshow(im)
ax[1][1].set_title('Lines')
for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
    (x0, y0) = dist * np.array([np.cos(angle), np.sin(angle)])
    ax[1][1].axline((x0, y0), slope=np.tan(angle + np.pi/2), c='red')

plt.show()
