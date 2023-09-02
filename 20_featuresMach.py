import cv2
from generalFunctions import show
import matplotlib.pyplot as plt
import numpy as np

"""
特征匹配
"""
"""
Brute-Force蛮力匹配
"""
img1 = cv2.imread('book.png')
img2 = cv2.imread('books.png')
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
"""
一对一
"""
bf = cv2.BFMatcher(crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
show(img3)
"""
k对最佳
"""
bf2 = cv2.BFMatcher()
matches = bf2.knnMatch(des1,des2,k=2)
good = []
for m,n in matches:
    if m.distance<0.75*n.distance:
        good.append([m])
img4 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
show(img4)
"""
如需更快，可以用cv2.FlannBasedMatcher
"""
"""
RANSAC在某些情况下比最小二乘要好一些，因为对离群点不敏感
"""

