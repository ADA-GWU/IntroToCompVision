import numpy as np
import cv2 as cv
from scipy import ndimage
from matplotlib import pyplot as plt

img = cv.imread('images/coffee3.jpeg',0)
#img = cv.imread('images/bigben1.jpg',0)
#img = cv.imread('/Users/jhasanov/Desktop/AICT-MRI/MRI_brain.png',0)
#img = cv.imread('/Users/jhasanov/Desktop/AICT-MRI/MRI-aug-orig.png',0)


w,h = img.shape
img_rot = ndimage.rotate(img,-10)
img_rot2 = ndimage.rotate(img,10)
#img_rot = ndimage.rotate(img[int(w/7):int(w/1.2),int(h/5):int(h/2)],45)
#img_rot = cv.imread('bigben2.jpg',0)

def get_orb_data(img):
    # find the keypoints with ORB
    kp = orb.detect(img,None)
 
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    return kp, des


# Initiate ORB detector
# https://docs.opencv.org/3.4/db/d95/classcv_1_1ORB.html#adc371099dc902a9674bd98936e79739c
orb = cv.ORB_create(nfeatures = 50, edgeThreshold=31,scoreType=cv.ORB_HARRIS_SCORE)

# draw only keypoints location,not size and orientation
kp1, des1 = get_orb_data(img)
img1 = cv.drawKeypoints(img, kp1, None, color=(0,255,0), flags=0)

kp2, des2 = get_orb_data(img_rot)
img2 = cv.drawKeypoints(img_rot, kp2, None, color=(0,255,0), flags=0)

kp3, des3 = get_orb_data(img_rot2)
img3 = cv.drawKeypoints(img_rot2, kp3, None, color=(0,255,0), flags=0)

# For feature matching
matcher = cv.BFMatcher()
matches = matcher.match(des1,des2)

final_img = cv.drawMatches(img, kp1, img_rot, kp2, matches[:50],None)


fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(13, 7))
ax[0][0].imshow(img1)
ax[0][0].set_title('Original')
ax[0][1].imshow(img2,cmap='gray')
ax[0][1].set_title('+10º rotation')
ax[1][0].imshow(img3,cmap='gray')
ax[1][0].set_title('-10º rotation')
ax[1][1].imshow(final_img)

plt.show()
