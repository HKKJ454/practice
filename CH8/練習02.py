import numpy as np
import cv2

def CMY_model(f, channel):
    if channel == 1:
        return 255 - f[:, :, 2]  #轉cyan(青色)
    elif channel == 2:
        return 255 - f[:, :, 1]  #轉magenta(紫紅)
    else:
        return 255 - f[:, :, 0]  #轉yellow(黃色)

def main():
    img = cv2.imread("egg.jpg", -1)
    C = CMY_model(img, 1)
    M = CMY_model(img, 2)
    Y = CMY_model(img, 3)
    cv2.imshow("Original Image", img)
    cv2.imshow("Cyan", C)
    cv2.imshow("Magenta", M)
    cv2.imshow("Yellow", Y)
    cv2.waitKey(0)

main()