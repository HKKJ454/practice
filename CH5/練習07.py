import numpy as np
from scipy.signal import convolve2d # 2D 卷積

x = np.array([[1, 1, 1], [1, 1, 1],[1, 1, 1]])
h = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
y = convolve2d(x, h,'same') # 對 x 和 h 做 2D 卷積，使用 'same' 模式
print("x =")
print(x)
print("h =")
print(h)
print("Convolution y =")
print(y)