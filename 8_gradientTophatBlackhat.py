import cv2
import numpy as np


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
梯度运算，本质上是膨胀减腐蚀,剩下轮廓
'''

kernel = np.ones((5, 5), np.uint8)
img = cv2.imread('test3.jpeg')
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
show('gradient', gradient)

'''
礼帽：原始-开运算结果，剩下毛刺
'''
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
show('tophat', tophat)

'''
黑帽：闭运算-原始输入,剩下一些小轮廓
'''
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
show('blackhat', blackhat)

'''
实验

'''
img1 = cv2.imread('test.jpg', 0)
# ret1, img1 = cv2.threshold(origin, 127, 255, cv2.THRESH_BINARY)  # 大于阈值的变成最大，小于等于阈值的变成0
result = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
show('result', result)
