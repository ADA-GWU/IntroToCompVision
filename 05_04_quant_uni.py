import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/colorbird.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img[25,25,:])



fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(13, 7))

# first one is for original
quant_val = [1,32,64,128]

for i in range(2):
	for j in range(2):
		ax[i][j].imshow((img//quant_val[i*2+j]) * quant_val[i*2+j])
		ax[i][j].set_title(str(quant_val[i*2+j]))


plt.show()

