import numpy as np
import cv2

img1= cv2.imread("central.jpg",-1)
nr,nc=img1.shape[:2]
pts1 = np.float32([[160, 165], [240, 390], [270, 125]]) #原圖上的三個點（來源點）
pts2 = np.float32([[190, 140], [190, 375], [310, 140]]) #變換後希望對應到的位置（目標點）
T= cv2.getAffineTransform(pts1, pts2)  #使用getAffineTransform()根據三個點對產生一個2×3仿射變換矩陣T
img2 = cv2.warpAffine(img1, T, (nc, nr)) #對原圖應用仿射矩陣T 輸出圖像大小設為原圖(nc, nr) 結果儲存在img2中
cv2.imshow("Original Image", img1)
cv2.imshow("Affine Transform", img2)
cv2.waitKey(0)
