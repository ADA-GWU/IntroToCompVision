import numpy as np
import cv2
from matplotlib import pyplot as plt

# window size
window_size = 40

# read two input images as grayscale images
imgL = cv2.imread('../images/TsukubaR.png',0)
imgR = cv2.imread('../images/TsukubaL.png',0)

dims = imgR.shape

# mouse callback function
def mouse_callback(event,x,y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: #cv2.EVENT_LBUTTONDBLCLK: 
        print('Clicked',x,y,dims)
        min_err = 1000000
        min_i   = 0

        leftBlock  = imgL[x-window_size//2:x+window_size//2,y-window_size//2:y+window_size//2]
        cv2.rectangle(imgL,(x-window_size//2,y-window_size//2),(x+window_size//2,y+window_size//2),(255,255,255),2)

        for i in range(window_size//2+1,dims[0]-2*window_size):
            rightBlock = imgR[i:i+window_size,y-window_size//2:y+window_size//2]
            err = ((leftBlock - rightBlock)**2).mean()
            #err = np.corrcoef(leftBlock, rightBlock).sum()
            if err < min_err:
                min_err = err
                min_i   = i
        print(min_i,min_err)
        cv2.rectangle(imgR,(min_i-window_size//2,y-window_size//2),(min_i+window_size//2,y+window_size//2),(255,255,255),2)
        plt.subplot(121),plt.imshow(imgL),plt.title('Left')
        plt.subplot(122),plt.imshow(imgR),plt.title('Right')
        plt.show()


cv2.namedWindow('image')
cv2.imshow("image",imgL)
cv2.setMouseCallback('image',mouse_callback)
while(1):    
    if cv2.waitKey(20) & 0xFF == 27: # Shift +Esc
        break
        cv2.destroyAllWindows
