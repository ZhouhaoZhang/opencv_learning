import cv2
from generalFunctions import show
import numpy as np

'''
高斯金字塔：用高斯核对原图进行上下采样
'''
origin = cv2.imread('test.jpg')
up = cv2.pyrUp(origin)
down = cv2.pyrDown(origin)
show('origin', origin)
show('up', up)
show('down', down)
updown = cv2.pyrDown(up)
res = np.hstack((origin, updown))
show('res', res)

'''
拉普拉斯金字塔：原图减去（下采样的上采样）
'''
downup = cv2.pyrUp(cv2.pyrDown(origin))
L1 = origin - downup
show('L1', L1)
