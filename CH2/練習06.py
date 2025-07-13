import numpy as np 
import cv2

img= cv2.imread("sea.jpg", -1)  #-1是原始影像
cv2.imshow("Example", img) #建立視窗並顯示影像
cv2.waitKey(0) #等待按鍵輸入
cv2.destroyAllWindows() #關閉所有視窗