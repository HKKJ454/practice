import numpy as np
import cv2

def image_downsampling(f, sampling_rate): #圖像下採樣 ,採樣間隔為sampling_rate
    nr, nc = f.shape[:2] #取得輸入圖像的高度（行數）和寬度（列數）
    nr_s, nc_s = nr // sampling_rate, nc // sampling_rate #計算降採樣後的圖像大小（高和寬都會變小）
    g = np.zeros([nr_s, nc_s], dtype='uint8') #建立一個降採樣後的圖像 g，大小為 nr_s x nc_s，所有像素初始值為0
    for x in range(nr_s):
        for y in range(nc_s):
            g[x, y] = f[x * sampling_rate, y * sampling_rate] #將原圖像中每 sampling_rate 個像素取一個值，填入降採樣後的圖像 g 中
    #這樣的操作會使得降採樣後的圖像 g 中每個像素對應到原圖像 f 中的一個區域，從而實現降採樣的效果
    return g

def main():
    img1 = cv2.imread("duck.jpg", 0)  # 以灰階讀取圖片
    if img1 is None:
        print("圖片讀取失敗，請確認檔名與路徑是否正確")
        return

    img2 = image_downsampling(img1, 2)

    cv2.imshow("Original Image", img1)
    cv2.imshow("Downsampling by 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()