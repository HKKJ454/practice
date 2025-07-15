import numpy as np
import cv2

def image_formation_model(f, x0, y0, sigma):
    g = f.copy()
    nr, nc = f.shape[:2]
    illumination = np.zeros((nr, nc), dtype='float32')

    for x in range(nr):
        for y in range(nc):
            illumination[x, y] = np.exp(-((x - x0) ** 2 + (y - y0) ** 2) / (2 * sigma ** 2))

    for x in range(nr):
        for y in range(nc):
            for k in range(3):  # RGB 通道
                val = round(illumination[x, y] * f[x, y, k])
                g[x, y, k] = np.uint8(np.clip(val, 0, 255))  # 限制在 0~255

    return g

def main():
    img = cv2.imread("Monet.bmp", -1)  # 讀取圖像
    if img is None:
        print("圖像讀取失敗，請確認檔案路徑與檔名是否正確")
        return

    nr, nc = img.shape[:2]
    x0 = nr // 2  # 中心點 x
    y0 = nc // 2  # 中心點 y
    sigma = 400

    img2 = image_formation_model(img, x0, y0, sigma)

    cv2.imshow("Original Image", img)
    cv2.imshow("Image Formation Model", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()