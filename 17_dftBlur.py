import cv2
import matplotlib.pyplot as plt
import numpy as np

from generalFunctions import bgr2rgb

'''
傅立叶变换：
    高频：变化剧烈的灰度分量，例如边界
    低频：变化缓慢的灰度分量，例如一片大海 

滤波：
    低通滤波器：只保留低频，会使得图像模糊
    高通滤波器：只保留高频，会使得图像细节增强
    
opencv中主要是cv2.dft()和cv2.idft(), 输入图像首先需要转换成np.float32格式
得到的结果中频率为0的部分会在左上角，通常需要转换到中心位置，可以通过shift变换实现。
cv2.dft() 返回的结果是双通道的（实部，虚部），通常还需要转换成图像格式才能展示
'''
img = cv2.imread('hist.jpg', 0)
img_bgr = cv2.imread('hist.jpg')
img_rgb = bgr2rgb(img_bgr)
img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)  # 傅立叶变换
dft_shift = np.fft.fftshift(dft)  # 调用shift方法将低频部分转移到中心位置
# 将傅立叶变换结果映射到一个单通道二维数组中
magnitude_specturm = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
Y, X = img.shape
center_y, center_x = int(Y / 2), int(X / 2)  # 中心位置

"""
高/低通滤波步骤：
    按照灰度方法读取原图
    将图片转换成float_32格式
    傅立叶变换
    调用shift方法将低频部分放到中间位置
    制作mask，把想漏出来的频率部分置1，想滤掉的频率部分置0
    mask与shift后的频谱做卷积
    逆shift
    逆傅立叶变换
    映射为可视化的二维单通道数组
"""
# 低通滤波
mask = np.zeros((Y, X, 2), np.uint8)
mask[center_y - 10:center_y + 10, center_x - 10:center_x + 10] = 1
# 可以理解为一个mask遮在频域图上，把中心的低频部分漏出来了
# asdjalfs;
# 逆傅立叶变换
fshift = dft_shift * mask  # 频谱图与mask做卷积，保留低频部分
f_ishift = np.fft.ifftshift(fshift)  # 逆shift
img_low_pass_back = cv2.idft(f_ishift)  # 逆傅立叶变换
img_low_pass_back = cv2.magnitude(img_low_pass_back[:, :, 0], img_low_pass_back[:, :, 1])  # 实部虚部处理成可视化图像

# 高通滤波
mask = np.ones((Y, X, 2), np.uint8)
mask[center_y - 30:center_y + 30, center_x - 30:center_x + 30] = 0
fshift = mask * dft_shift
f_ishift = np.fft.ifftshift(fshift)
img_high_pass_back = cv2.idft(f_ishift)
img_high_pass_back = cv2.magnitude(img_high_pass_back[:, :, 0], img_high_pass_back[:, :, 1])

# 展示
plt.subplot(321), plt.imshow(img_rgb), plt.title('Image_RGB'), plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(magnitude_specturm), plt.title('Frequency'), plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(img, 'gray'), plt.title('Image_GRAY'), plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(img_low_pass_back,'gray'), plt.title('Low_pass blur'), plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(img_high_pass_back,'gray'), plt.title('high_pass blur'), plt.xticks([]), plt.yticks([])
plt.subplot(324)
color = ('b', 'g', 'r')
for i, col in enumerate(color):  # 枚举
    histr = cv2.calcHist([img_bgr], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title('Hist')
plt.show()
