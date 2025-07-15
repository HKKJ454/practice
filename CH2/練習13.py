import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # 建立一張黑色圖片 (512x512,3通道, uint8類型)

# 定義畫線的參數
pt1 = (50, 50) # 起點
pt2 = (400, 400) # 終點
color = (255, 0, 0)       # 綠色
thickness = 3             # 線的粗細
lineType = cv2.LINE_8     # 線型（也可以不加，預設就是 LINE_8）
shift = 0                 # 預設是 0

# 畫線
cv2.line(img, pt1, pt2, color, thickness, lineType, shift)

# 顯示結果
cv2.imshow("Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 #顏色            BGR 值           
# 黑色           (0, 0, 0)       
# 白色           (255, 255, 255) 
# 紅色           (0, 0, 255)     
# 綠色           (0, 255, 0)     
# 藍色           (255, 0, 0)     
# 黃色           (0, 255, 255)   
# 品紅（洋紅）    (255, 0, 255)   
#青色（青綠）    (255, 255, 0)   
