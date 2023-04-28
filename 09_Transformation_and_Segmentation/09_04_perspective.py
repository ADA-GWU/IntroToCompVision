import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

points = 4
pts1 = np.zeros((points,2), dtype=np.float32)
inputs = 0

img = cv.imread('images/sudoku.jpg')
h,w,ch = img.shape

def persp_transf():
    global inputs
    inputs = 0

    w = int(pts1[3,0]-pts1[2,0])
    #h = int(pts1[3,1]-pts1[0,1])
    
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    print(pts2)

    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(w,h))

    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

def mouse_callback(event,x,y, flags, param):
    global pts1, inputs

    if event == cv.EVENT_LBUTTONDOWN:
        pts1[inputs,0] = x
        pts1[inputs,1] = y
        cv.circle(img,(x,y),2,(0,0,255),-1)

        inputs += 1
        if inputs == points:
            print(pts1)
            cv.destroyAllWindows()
            persp_transf()


cv.namedWindow('image')
cv.setMouseCallback('image',mouse_callback)

while(1):
    cv.imshow("image",img)
    if cv.waitKey(20) & 0xFF == 27: # Shift +Esc
        break
cv.destroyAllWindows
