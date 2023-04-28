import rasterio
import matplotlib.pyplot as plt

fp = r'/Users/jhasanov/Downloads/MultiBandGeoData.tif'
img = rasterio.open(fp)

print('Count:',img.count)
print('Height:',img.height,'Width:',img.width)
print('Coordinate Reference System:',img.crs)

f, axarr = plt.subplots(3,4) 

for i in range(3):
	for j in range(4):
		axarr[i,j].imshow(img.read(i*4+j+1), cmap='gray')

plt.show() 
