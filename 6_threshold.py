import cv2


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
阈值
'''

img = cv2.imread('test.jpg', 0)
ret1, img1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 大于阈值的变成最大，小于等于阈值的变成0
ret2, img2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 上面的反转
ret3, img3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)  # 大于阈值的变成阈值，小于等于阈值的不变
ret4, img4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # 大于阈值的不变，小于等于阈值的变成0
ret5, img5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 上面的反转

show('0', img)
show('1', img1)
show('2', img2)
show('3', img3)
show('4', img4)
show('5', img5)
