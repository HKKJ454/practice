import numpy as np 
import cv2 

global img #定義img為全域變數 
def onMouse(event, x, y, flags, param):  
#event:表示滑鼠事件（如點擊、移動等）
#x,y:表示滑鼠事件發生的位置（座標）
#flags:附加鍵的狀態（如 Shift、Ctrl 等）
#param:額外參數（這裡沒用到）
    x,y = y,x #將x,y座標對調，因為OpenCV是BGR而三原色是RGB
    if img.ndim !=3:  #檢查圖像是否為灰階
          print("(x,y)=(%d,%d)" %(x,y),end=" ") #輸出座標 %d表示整數 %(x,y)表示格式化輸出
          print("Gray-Level=%3d" %img[x,y]) #輸出灰階值 %3d表示三位數的整數(對齊)
        #%img[x,y]表示取出座標(x,y)的灰階值
    else:
          print("(x,y)=(%d,%d)" %(x, y),end=" ") #輸出座標
          print("(R,G,B)=(%3d,%3d,%3d)" % #輸出RGB值
               (img[x,y,2],img[x,y,1],img[x,y,0])) #輸出BGR值 
          #img[x,y,2]表示紅色通道的值 img[x,y,1]表示綠色通道的值 img[x,y,0]表示藍色通道的值

filename=input("Please enter filename:")
img = cv2.imread(filename,-1)
cv2.namedWindow(filename) #創建一個窗口
cv2.setMouseCallback(filename, onMouse) #設置鼠標回調函數
cv2.imshow(filename, img) #顯示圖像
cv2.waitKey(0) #等待按鍵事件