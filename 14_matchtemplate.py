import cv2
import numpy as np
from matplotlib import pyplot as plt


def display(bedrew, result):
    b, g, r = cv2.split(bedrew)  # 颜色通道提取
    match_result_rgb = cv2.merge((r, g, b))  # 颜色通道合并
    plt.subplot(121), plt.imshow(result)
    plt.subplot(122), plt.imshow(match_result_rgb)
    plt.suptitle(meth)
    plt.show()


'''
模版匹配，输入原图A*B，模版a*b，输出矩阵尺寸为(A-a+1)*(B-b+1)
'''
origin = cv2.imread('test.jpg', 0)
model = cv2.imread('test_part.jpg', 0)

methods = {'cv2.TM_SQDIFF', 'cv2.TM_CCORR', 'cv2.TM_CCOEFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR_NORMED',
           'cv2.TM_CCOEFF_NORMED'}
'''
    TM_SQDIFF 计算平方不同，计算出的值越小越相关
    TM_CCORR 计算相关性，越大越相关
    TM_CCOEFF 计算相关系数，越大越相关
    TM_SQDIFF_NORMED 计算归一化平方不同，越接近0越相关
    TM_CCORR_NORMED 计算归一化相关性，越接近1越相关
    TM_CCOEFF_NORMED 计算归一化相关系数，越接近1越相关
'''
(y, x) = model.shape
for meth in methods:
    img = cv2.imread('test.jpg')
    method = eval(meth)
    res = cv2.matchTemplate(origin, model, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 区别对待
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        (X, Y) = min_loc
    else:
        (X, Y) = max_loc

    # 画框
    match_result = cv2.rectangle(img, (X, Y), (X + x, Y + y), (0, 0, 255), 8)
    # plot函数支持的是RGB模式
    display(match_result, res)

'''
匹配多个对象
'''
origin = cv2.imread('mario.jpg', 0)
model = cv2.imread('coin.jpg', 0)
match_result = None
(y, x) = model.shape
for meth in methods:
    img = cv2.imread('mario.jpg')
    method = eval(meth)
    res = cv2.matchTemplate(origin, model, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 区别对待
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        threshold = 0.1
        loc = np.where(res <= threshold*max_val)
    else:
        threshold = 0.95
        loc = np.where(res >= threshold*max_val)

    for pt1 in zip(*loc[::-1]):
        pt2 = (pt1[0] + x, pt1[1] + y)
        # 画框
        match_result = cv2.rectangle(img, pt1, pt2, (0, 0, 255), 2)

    display(match_result, res)
