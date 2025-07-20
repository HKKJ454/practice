import numpy as np
import cv2

img1 = cv2.imread("central.jpg", -1)

nr, nc = img1.shape[:2]
scale = eval(input("Please enter scale: ")) #輸入縮放比例
nr2 = int(nr * scale)  #根據縮放比例計算新的行數
nc2 = int(nc * scale) #根據縮放比例計算新的列數
img2 = cv2.resize(img1,(nr2, nc2),interpolation=cv2.INTER_LINEAR) #使用線性插值法進行縮放「雙線性插值」方式縮放（效果平滑，適合放大縮小）
cv2.imshow("Original Image", img1)
cv2.imshow("Image Scaling", img2)
cv2.waitKey(0)  