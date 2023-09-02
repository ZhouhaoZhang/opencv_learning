import cv2
import matplotlib.pyplot as plt
import numpy as np

from generalFunctions import show

img = cv2.imread('test.jpg', 0)
# 均衡化
equ_img = cv2.equalizeHist(img)

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.hist(img.ravel(), 256)
plt.subplot(223), plt.imshow(equ_img, 'gray')
plt.subplot(224), plt.hist(equ_img.ravel(), 256)
plt.xlim([0, 256])
plt.show()

# 自适应直方图均衡化（一般的均衡化可能会丢失细节，自适应均衡化可以避免）
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
auto_equ_img = clahe.apply(img)
res = np.hstack((img, equ_img, auto_equ_img))

plt.imshow(res,'gray')
plt.show()

show('res', res)
