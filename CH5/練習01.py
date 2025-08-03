import numpy as np
import cv2

def image_negative(f): #
    g = 255 - f  # 將圖像轉換為負片 原像素是 100，負片就是 155（因為 255 - 100 = 155）   
#這會把亮的變暗，暗的變亮，整張圖像色彩反轉
    return g

def main():
    img1 = cv2.imread("cute.jpg", -1)  # 讀取圖像（包含alpha channel）
    img2 = image_negative(img1)         # 轉換成負片
    cv2.imshow("Original Image",img1)  
    cv2.imshow("Image Negative",img2)  
    cv2.waitKey(0)                     
        
main()