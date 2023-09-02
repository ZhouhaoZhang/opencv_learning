import cv2


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


'''
数值计算
'''
img = cv2.imread('test.jpg')
img1 = img + 10000
show('result', img1)

img2 = img + img
show('img+img', img2)

img3 = cv2.add(img, img)
show('img3', img3)
