import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram(f):
     if f.ndim == 3:
            hist = cv2.calcHist([f],[0], None, [256], [0, 256])
            plt.plot(hist)  # 使用黑色線條
     else:  
           color = ('b', 'g', 'r')  # OpenCV 是 BGR 順序
           for i,col in enumerate(color):
     hist = cv2.calcHist(f, [i], None, [256], [0,256])
     plt.plot(hist, color=col)
     plt.xlim([0, 256])
     plt.xlabel("Intensity")
     plt.ylabel("#Intensity")
     plt.show()

def main():
    img = cv2.imread("cute.jpg", -1) 
    cv2.imshow("Original Image", img)
    histogram(img)

main()