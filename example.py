from draw import drawAb
import math
from selectOT import Select
# # x = Select(1.03, 255, 260, 40, 263, 1.19, 6.9, 0.015, 1.77, 8, 0.33, 3)
# # print(x.slove())

# 药柱筛选
x = Select(1.03, 265, 260, 40, 263, 1.19, 6.9, 0.015, 1.77, 8, 0.33, 8, 8, 1.2, 1, (0.75, 0.85), 5)
# 第五次筛选结果
print(x.slove5())
print(x.halfthetadic)

# 画燃面随时间变化的图
x = drawAb()
x.drawallpiv(1, 3, 0.4, 17.347*2/180 *math.pi, 3.975, 8, 74.965, 0.426, 1.408)
x.drawallpiv(2, 4, 0.5, 20.159*2/180 *math.pi, 3.975, 8, 74.965, 0.408, 1.410)
x.drawallpiv(3, 5, 0.6, 22.735*2/180 *math.pi, 3.975, 8, 74.965, 0.399, 1.410)
x.drawallpiv(4, 6, 0.7, 25.1*2/180 *math.pi, 3.975, 8, 74.965, 0.396, 1.408)
x.drawallpiv(5, 7, 0.7, 23.877*2/180 *math.pi, 3.975, 8, 74.965, 0.338, 1.432)
x.drawallpiv(6, 7, 0.8, 27.276*2/180 *math.pi, 3.975, 8, 74.965, 0.395, 1.405)
x.drawallpiv(7, 8, 0.8, 26.225*2/180 *math.pi, 3.975, 8, 74.965, 0.344, 1.426)
x.picshow()