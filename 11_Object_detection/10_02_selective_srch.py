#https://pyimagesearch.com/2020/06/29/opencv-selective-search-for-object-detection/
import argparse
import random
import time
import cv2
from matplotlib import pyplot as plt

method = "slow" # fast/slow
image_file = "images/human_and_dog.jpg"

image = cv2.imread(image_file)

# initialize OpenCV's selective search implementation and set the input image
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image)

# check to see if we are using the *fast* but *less accurate* version
# of selective search
if method == "fast":
	print("[INFO] using *fast* selective search")
	ss.switchToSelectiveSearchFast()
# otherwise we are using the *slower* but *more accurate* version
else:
	print("[INFO] using *quality* selective search")
	ss.switchToSelectiveSearchQuality()

# run selective search on the input image
start = time.time()
rects = ss.process()
end = time.time()

# show how along selective search took to run along with the total
# number of returned region proposals
print("[INFO] selective search took {:.4f} seconds".format(end - start))
print("[INFO] {} total region proposals".format(len(rects)))

# loop over the region proposals in chunks (so we can better visualize them)
for i in range(0, len(rects), 100):
	# clone the original image so we can draw on it
	output = image.copy()
	# loop over the current subset of region proposals
	for (x, y, w, h) in rects[i:i + 100]:
		# draw the region proposal bounding box on the image
		color = [random.randint(0, 255) for j in range(0, 3)]
		cv2.rectangle(output, (x, y), (x + w, y + h), color, 2)
	# show the output image
	plt.imshow(output)

plt.show()
