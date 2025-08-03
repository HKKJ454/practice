import numpy as np
import cv2

def gamma_correction(f, gamma=2.0): #這個函式會對輸入影像 f 進行 Gamma 校正，gamma 預設值是 2.0
    g= f.copy() # 先複製輸入影像 f 到 g
    nr, nc = f.shape[:2]  
    c = 255.0 / (255.0 ** gamma) # 計算常數c，這個常數用來調整影像的亮度 
    # gamma < 1：整張圖會變亮 gamma > 1：整張圖會變暗
    table = np.zeros(256) # 建立一個長度為 256 的陣列，用來存放每個像素值經過 Gamma 校正後的值
    for i in range(256): 
        table[i] = round(i**gamma*c,0) #這裡建立一個對照表 table，先把 0~255 的每個值做 Gamma 處理，這樣後面查表比每次算公式更快
    if f.ndim !=3:  #檢查影像是否為灰階圖像
        for x in range(nr): #灰階處理
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:   #如果是彩色圖像
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    return g

def main():
    img = cv2.imread("cute.jpg", 0)  # 讀入灰階圖像
    img1 = gamma_correction(img, 0.1)
    img2 = gamma_correction(img, 0.2)
    img3 = gamma_correction(img, 0.5)
    cv2.imshow("Original Image", img)
    cv2.imshow("Gamma = 0.1", img1)
    cv2.imshow("Gamma = 0.2", img2)
    cv2.imshow("Gamma = 0.5", img3)
    cv2.waitKey(0)


main()