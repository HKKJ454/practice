import numpy as np
import cv2

def image_quantization(f, bits): #影像量化，bits=5：將影像量化為 32 階灰階
    g = f.copy()
    nr, nc = f.shape[:2]
    levels = 2 ** bits   # 灰階等級，例如 bits=5，levels=32 階                       # 量化等級，例如 bits=5 時 levels=32
    interval = 256 / levels # 每階區段寬度，例如 256/32 = 8                    # 每個區段的寬度
    gray_level_interval = 255 / (levels - 1)    # 每一階代表的灰階值
    table = np.zeros(256) # 建立一個對應表，將每個灰階值映射到量化後的灰階值
    for k in range(256): # 對於每個灰階值
        for l in range(levels): # 對於每個量化等級
            if k >= l * interval and k < (l + 1) * interval: # 判斷灰階值 k 落在哪個區段
                table[k] = round(l * gray_level_interval) # 將灰階值 k 映射到對應的量化後灰階值
    for x in range(nr):
        for y in range(nc):
            g[x, y] = np.uint8(table[f[x, y]]) # 使用對應表將原圖像的灰階值轉換為量化後的灰階值
    return g

def main():
    img1 = cv2.imread("duck.jpg", -1)  # 以灰階讀取圖片
    img2 = image_quantization(img1,5)  # bits=5：將影像量化為 32 階灰階
    cv2.imshow("Original Image", img1)
    cv2.imshow("Quantization", img2)
    cv2.waitKey(0)

main()