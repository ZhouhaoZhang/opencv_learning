import cv2
import numpy as np
from generalFunctions import show
'''
Canny边缘检测
    1 使用高斯滤波器去除噪声
    2 计算每个像素点的梯度和方向
    3 应用非极大值抑制消除边缘检测带来的杂散响应
    4 应用双阈值检测来确定真实的和潜在的边缘
    5 通过抑制孤立的弱边缘最终完成边缘检测
'''

origin = cv2.imread('test.jpg', 0)
res1 = cv2.Canny(origin, 140, 150)# MinValue和MaxValue
res2 = cv2.Canny(origin, 10, 20)
res = np.hstack((origin,res1 ,res2))
show(res,'res')
