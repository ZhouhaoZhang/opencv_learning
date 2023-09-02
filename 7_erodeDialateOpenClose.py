import cv2
import numpy as np


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
腐蚀操作
'''

img = cv2.imread('test3.jpeg')
show('origin', img)

kernel = np.ones((10, 10), np.uint8)  # 产生卷积核

erosion = cv2.erode(img, kernel, iterations=3)  # 迭代次数
show('erosion', erosion)

'''
膨胀操作
'''
dilate = cv2.dilate(img, kernel, iterations=3)
show('dilate', dilate)

'''
开运算：先腐蚀再膨胀
'''
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
show('opening', opening)

'''
闭运算：先膨胀再腐蚀
'''
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
show('closing', closing)
