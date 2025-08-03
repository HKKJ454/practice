import numpy as np
import cv2

def composite_laplacian(f):
    kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]]) # Composite Laplacian 核心：中心為 +5，周圍為 -1
    temp = cv2.filter2D(f, cv2.CV_32F, kernel) # 使用 filter2D 濾波
    g = np.uint8(np.clip(temp, 0, 255))     # 將結果剪裁並轉換為 uint8 型別
    return g

def main():
    img1 = cv2.imread("cute.jpg", -1)
    img2 = composite_laplacian(img1)
    cv2.imshow("Original Image", img1)
    cv2.imshow("Composite Laplacian", img2)
    cv2.waitKey(0)

main()