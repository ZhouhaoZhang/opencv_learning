import cv2
import numpy as np

from OpenCV_learning.generalFunctions import show

"""
角点检测
cv2.cornerHarris()
    img: 数据类型为float32的输入图像
    blockSize：角点检测中制定区域的大小
    ksize：Sobel求导中使用窗口的大小 一般3
    k：取值参数为[0.04, 0.06] 一般0.04
"""
img = cv2.imread('chessboard.jpeg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray)
dst = cv2.cornerHarris(img_gray, 10, 3, 0.04)
print(dst)
img[dst > 0.5 * dst.max()] = [0, 0, 255]  # 索引条件越苛刻，得到的角点信息越少
show('res', img)
