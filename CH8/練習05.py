import numpy as np
import cv2

def YCrCb_model(f, channel):
    ycrcb = cv2.cvtColor(f, cv2.COLOR_BGR2YCrCb)
    if channel == 1:      # Y(亮度)
        return ycrcb[:, :, 0]
    elif channel == 2:    # Cr(紅色的偏移量)
        return ycrcb[:, :, 1]
    else:                 # Cb(藍色的偏移量)
        return ycrcb[:, :, 2]

def main():
    img = cv2.imread("egg.jpg", -1)
    Y = YCrCb_model(img, 1)
    Cr = YCrCb_model(img, 2)
    Cb = YCrCb_model(img, 3)
    cv2.imshow("Original Image", img)
    cv2.imshow("Y", Y)
    cv2.imshow("Cr", Cr)
    cv2.imshow("Cb", Cb)
    cv2.waitKey(0)

main()