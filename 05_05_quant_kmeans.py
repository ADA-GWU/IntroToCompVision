import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/colorbird.jpg')

z = img.reshape((-1,3))

# convert to np.float32
z = np.float32(z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)



fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(13, 7))

# first one is for original
quant_val = [32,16,8,4]

for i in range(2):
	for j in range(2):
		ret,label,center=cv2.kmeans(z,quant_val[i*2+j],None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

		# Convert back into uint8, and make original image
		center = np.uint8(center)
		res = center[label.flatten()]
		res2 = res.reshape((img.shape))

		ax[i][j].imshow(res2)
		ax[i][j].set_title(str(quant_val[i*2+j]))


plt.show()
