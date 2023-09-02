import cv2
from generalFunctions import show
import numpy as np

'''
图像轮廓
    cv2.findContours(img,mode,method)
    mode :轮廓检索模式：
        RETR_EXTERNAL:只检测最外面的轮廓
        RETR_LIST:检索所有轮廓，并将其保存在一条链表当中
        RETR_CCOMP:检索所有轮廓，并将它们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界
      * RETR_TREE:检索所有轮廓，并重构嵌套轮廓的整个层次
    method:轮廓的逼近方法：
        CHAIN_APPROX_NONE:以Freeman链码的方式输出轮廓，所有其他方法输出多边形（定点的序列）
        CHAIN_APPROX_SIMPLE:压缩水平的，垂直的和斜的部分，只保留它们的终点的部分
'''
origin = cv2.imread('test3.jpeg')
grey_origin = cv2.imread('test3.jpeg', 0)
# 二值化处理
ret, thresh = cv2.threshold(grey_origin, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

draw_img = origin.copy()
res1 = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 8)  # -1 代表输出所有轮廓，2 代表宽度
show(res1)

'''
轮廓特征
'''
cnt = contours[0]
# 面积
S = cv2.contourArea(cnt)
# 周长，True表示闭合的
L = cv2.arcLength(cnt, True)
print('面积是', S)
print('周长是', L)

'''
轮廓近似
'''
draw_img = origin.copy()
i = 0
res2 = None
while i < len(contours):
    cnt = contours[i]
    epsilon = 0.03 * cv2.arcLength(cnt, True)  # epsilon占周长的比例
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    res2 = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 5)
    i = i + 1
'''
外接矩形
'''
res3 = None
i = 0
origin_copy1 = origin.copy()
while i < len(contours):
    cnt = contours[i]
    x, y, w, h = cv2.boundingRect(cnt)
    res3 = cv2.rectangle(origin_copy1, (x, y), (x + w, y + h), (0, 0, 255), 5)
    i = i + 1
    # 面积比
    cnt_area = cv2.contourArea(cnt)
    box_area = w * h
    ratio = cnt_area / box_area
    print("第{0}个轮廓占边框{1}".format(i, ratio))

# show('res3', res3)

'''
外接圆
'''
origin_copy2 = origin.copy()
res4 = None
i = 0
while i < len(contours):
    cnt = contours[i]
    (x, y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    r = int(r)
    res4 = cv2.circle(origin_copy2, center, r, (0, 0, 255), 5)
    i = i + 1

res = np.hstack((res1, res2, res3, res4))
show('res', res)
