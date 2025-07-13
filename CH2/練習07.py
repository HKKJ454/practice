import numpy as np 
import cv2

img= cv2.imread("sea.jpg", 0) # 0表示讀取為灰階影像 
cv2.imshow("Example", img)
cv2.waitKey(1000) # 等待1000毫秒
cv2.destroyAllWindows() 