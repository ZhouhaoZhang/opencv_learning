import cv2


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
色彩空间转换
'''
img = cv2.imread('test.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
show('img1', img1)

'''
图像融合
'''
img3 = cv2.resize(img, (800, 600))
img4 = cv2.resize(img1, (800, 600))
img5 = cv2.addWeighted(img3, 0.4, img4, 0.6, 0)
show('img5', img5)
