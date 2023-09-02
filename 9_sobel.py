import cv2
from generalFunctions import show as s

'''
def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
'''

origin = cv2.imread('test3.jpeg')
# 计算X方向梯度
sobelx = cv2.Sobel(origin, cv2.CV_64F, 1, 0, ksize=3)  # cv2.CV_64F表示图像的深度
abs_sobelx = cv2.convertScaleAbs(sobelx)  # 取绝对值
s('sobelx', sobelx)
s('abs_sobelx', abs_sobelx)
# 计算Y方向梯度
sobely = cv2.Sobel(origin, cv2.CV_64F, 0, 1, ksize=3)
abs_sobely = cv2.convertScaleAbs(sobely)
s('sobely', sobely)
s('abs_sobely', abs_sobely)

# x，y方向梯度求和
sobelxy = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
s('sobelxy', sobelxy)
'''
不建议直接用sobel方法同时计算Gx和Gy，效果可能不好，分别计算Gx和Gy再融合效果好
'''

'''
实验
'''
img = cv2.imread('test.jpg', 0)
ret, img0 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 二值化
sobelx = cv2.Sobel(img0, cv2.CV_64F, 1, 0, ksize=3)
abs_sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img0, cv2.CV_64F, 0, 1, ksize=3)
abs_sobely = cv2.convertScaleAbs(sobely)
result = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
s('result', result)
