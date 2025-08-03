import numpy as np 
import cv2

img1= cv2.imread("cute.jpg", 0)
img2= cv2.equalizeHist(img1) #對灰階影像 img1 執行「直方圖均衡化」
cv2.imshow("Original Image", img1)
cv2.imshow("Histogram Equalization", img2)
cv2.waitKey(0)