import numpy as np
import cv2

def laplacian(f):
    temp = cv2.Laplacian(f, cv2.CV_32F) + 128 # 計算 Laplacian，並將值加上 128 做偏移以避免負值
    g = np.uint8(np.clip(temp, 0, 255)) # 將結果剪裁並轉換為 uint8 型別
    return g

def main():
    img1 = cv2.imread("cute.jpg", -1)  # -1 表示保留原圖通道
    img2 = laplacian(img1) # 計算 Laplacian
    cv2.imshow("Original Image", img1)
    cv2.imshow("Laplacian", img2)
    cv2.waitKey(0)

main()