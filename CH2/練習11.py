import numpy as np 
import cv2 

global img #定義img為全域變數 
def onMouse(event, x, y, flags, param):  
    x,y = y,x #將x,y座標對調，因為OpenCV是BGR而三原色是RGB
    if img.ndim !=3: 
          print("(x,y)=(%d,%d)" %(x, y),end=" ")
          print("Gray-Level=%3d" % img[x,y])
    else:
          print("(x,y)=(%d,%d)" % (x, y),end=" ")
          print("(R,G,B)=(%3d,%3d,%3d)" % 
               (img[x,y,2], img[x,y,1], img[x,y,0]))

filename=input("Please enter filename:")
img = cv2.imread(filename, 0) #讀取圖像，0表示灰階模式
cv2.namedWindow(filename)
cv2.setMouseCallback(filename, onMouse)
cv2.imshow(filename, img)
cv2.waitKey(0)