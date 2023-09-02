import cv2
from generalFunctions import show

'''
边界填充
'''
img = cv2.imread('test.jpg')
top_size, bottom_size, right_size, left_size = (300, 280, 210, 230)
img1 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT, value=-1)
img2 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_DEFAULT)
img3 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REPLICATE)
img4 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
img5 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
img6 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_ISOLATED)
img7 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT101)
img8 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
show('constant', img1)
show('default', img2)
show('replace', img3)
show('reflect', img4)
show('wrap', img5)
show('isolated', img6)
show('reflect101', img7)
show('reflect_101', img8)
