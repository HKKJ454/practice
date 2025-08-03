import numpy as np

x = np.array([1, 2, 4, 3, 2, 1, 1]) 
h = np.array([1, 2, 3, 1, 1])
y = np.convolve(x, h, 'full') #對 x 和 h 做 完整卷積（full convolution），包含所有可能的重疊區域
y1 = np.convolve(x, h, 'same') #對 x 和 h 做 相同長度卷積（same convolution），輸出與 x 長度相同
print("x =", x)
print("h =", h)
print("Full Convolution y =", y)
print("Convolution y1 =", y1)