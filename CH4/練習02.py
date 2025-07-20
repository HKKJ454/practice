import numpy as np
import cv2

img= cv2.imread("central.jpg",0)
nr1,nc1=img.shape[:2] 
nr2,nc2=nr1//4,nc1//4 #將圖像和高度都縮小為原來的1/4
img1 = cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_NEAREST) #先用「最近鄰法」縮小
img1 = cv2.resize(img1,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #再用「最近鄰法」放大回原來的大小
img2 = cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_LINEAR)  #先用「雙線性法」縮小
img2 = cv2.resize(img2,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #再用「最近鄰法」放大
img3 = cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_CUBIC)# 雙三次縮小再放大
img3 = cv2.resize(img2,(nr1,nc1),interpolation=cv2.INTER_NEAREST) #再用「最近鄰法」放大
cv2.imshow("Original Image", img)
cv2.imshow("Nearest Neighbor", img1) #最近鄰法
cv2.imshow("Bilinear", img2) #雙線性法
cv2.imshow("Bicubic", img3) #雙三次法
cv2.waitKey(0)