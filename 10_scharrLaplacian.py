import cv2
import numpy as np
from generalFunctions import show as sh


def compare(image):
    origin = cv2.imread(image, 0)
    sobelx = cv2.Sobel(origin, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(origin, cv2.CV_64F, 0, 1, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    sobely = cv2.convertScaleAbs(sobely)
    sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    scharrx = cv2.Scharr(origin, cv2.CV_64F, 1, 0)
    scharry = cv2.Scharr(origin, cv2.CV_64F, 0, 1)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.convertScaleAbs(scharry)
    scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

    laplacian = cv2.Laplacian(origin, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)

    result = np.hstack((origin, sobelxy, scharrxy, laplacian))
    sh('result', result)


compare('test.jpg')
compare('test2.jpeg')
compare('test3.jpeg')

'''
Sobel算子对常规边缘敏感
Scharr算子对边缘和纹理都敏感
Laplacian算子对噪音点很敏感，一般要和别的东西配合使用
'''
