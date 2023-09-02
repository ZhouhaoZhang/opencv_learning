import cv2


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
滤波
'''

img = cv2.imread('test2.jpeg')
show('origin', img)

# 均值滤波 简单平均卷积操作 相当于归一化的方框滤波
img1 = cv2.blur(img, (3, 3))
show('blur', img1)

# 高斯滤波 离得近的权重大

img2 = cv2.GaussianBlur(img, (5, 5), 1)
show('gauss', img2)

# 中值滤波
img3 = cv2.medianBlur(img, 5)
show("median", img3)
