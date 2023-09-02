import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hist.jpg', 0)
BIN = 256
hist = cv2.calcHist([img], [0], None, [BIN], [0, 256])  # 返回一个BIN维向量
'''
images 原图格式为uint8或者float32。当传入函数时应该使用[]括起来
channels 灰度图就填[0],彩色图就填入[0],[1],[2]分别代表BGR
mask 掩模，统计整个图就用None，统计部分图就制作一个掩模传进去
histSize BIN的数目，也用[]括起来
ranges 像素值范围，常为[0, 256]
'''
plt.hist(img.ravel(), 256)  # matplot可以直接画直方图
plt.show()
plt.plot(hist)  # matplot画统计图，hist是一个列向量
plt.show()

# 画出BGR三个通道的直方图
img = cv2.imread('hist.jpg')
img = cv2.resize(img, (400, 300))
color = ('b', 'g', 'r')
for i, col in enumerate(color):  # 枚举
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
plt.xlim([0, 256])
plt.show()

'''
有掩模情形下的直方图
'''
img = cv2.imread('hist.jpg', 0)
# 创建mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[1000:3000, 1000:4000] = 255
# show('mask', mask)
masked_img = cv2.bitwise_and(img, img, mask=mask)  # 与操作
# show('masked_img', masked_img)
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_masked = cv2.calcHist([img], [0], mask, [256], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_masked)
plt.xlim([0, 256])
plt.show()
