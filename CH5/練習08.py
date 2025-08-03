import numpy as np
import cv2

img1 = cv2.imread("cute.jpg",-1)  
img2 = cv2.blur(img1, (10, 10)) # 平均濾波，使用 10x10 的卷積核
cv2.imshow("Original Image", img1)
cv2.imshow("Average Filtering", img2)
cv2.waitKey(0)