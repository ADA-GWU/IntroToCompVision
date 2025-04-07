import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img_rgb = cv.imread('images/mastercard.png')
img_rgb = cv.imread('../images/playing_card.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

#template = cv.imread('images/mastercard-logo.png',0)
template = cv.imread('../images/clubs.jpg',0)

w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv.imshow('Result',img_rgb)

cv.waitKey(0)
cv.destroyAllWindows()
