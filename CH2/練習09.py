import numpy as np
import cv2

filename=input("Please enter filename:") 
img = cv2.imread(filename, -1) # -1:原始圖像, 0:灰階圖像, 1:彩色圖像
nr,nc=img.shape[:2] # 取得圖像的行數和列數 ,(高度, 寬度, 通道數)
print("Number of Rows:", nr) #行數
print("Number of Columns:", nc) #列數
if img.ndim !=3: #檢查圖像的維度
    print(" Gray-Level Image") #檢查圖像是否為灰階圖像
else:
    print(" Color Image") #檢查圖像是否為彩色圖像

