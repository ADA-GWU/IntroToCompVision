import rasterio
import matplotlib.pyplot as plt

fp = r'images/10bands.tiff'
fp = r'images/allbands.tiff'
img = rasterio.open(fp)

print('Count:',img.count)
print('Height:',img.height,'Width:',img.width)
print('Coordinate Reference System:',img.crs)
print('Tags:',img.tags())

f, axarr = plt.subplots(2,5) 


for i in range(2):
	for j in range(5):
		axarr[i,j].imshow(img.read(i*5+j+1),cmap='gray')

plt.show() 
