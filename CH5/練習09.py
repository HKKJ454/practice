import numpy as np
import cv2

# 讀取圖片（使用 -1 表示保留原始通道）
img1 = cv2.imread("cute.jpg", -1)

# 使用 5x5 核心做高斯模糊，標準差為 0（自動計算）
img2 = cv2.GaussianBlur(img1, (5, 5), 0)

# 顯示原始影像與模糊處理後的影像
cv2.imshow("Original Image", img1)
cv2.imshow("Gaussian Filtering", img2)
cv2.waitKey(0)
