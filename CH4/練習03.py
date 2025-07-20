import numpy as np
import cv2

img1= cv2.imread("central.jpg",-1)
nr2,nc2=img1.shape[:2] 
rotation_matrix = cv2.getRotationMatrix2D((nc2 /2, nr2 /2),30,1)  # 旋轉中心在圖像中心,順時針旋轉角度30度，縮放比例為1 
img2 = cv2.warpAffine(img1,rotation_matrix,(nc2, nr2))  # 使用仿射變換將圖像進行旋轉
cv2.imshow("Original Image", img1)
cv2.imshow("Image Rotation", img2)
cv2.waitKey(0)