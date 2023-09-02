import cv2

'''
基本操作：
图像读取，按灰度读取，展示，存储，ROI，通道提取与合并，视频读取与展示
'''


def show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


img1 = cv2.imread('test.jpg')  # 默认读入彩色图，BGR
img2 = cv2.imread('test.jpg', 0)  # 读入灰度图
# show('img1', img1)
# show('img2', img2)
print(img1)
print(img2)
print(img1.shape)  # h,w,c2.shape)  # h,w
print(type(img1))

cv2.imwrite('result.png', img2)  # 图像的保存
area = img1[100:2000 ,100:200]  # 截取部分图像，ROI区域 先y后x
show('area', area)
b, g, r = cv2.split(img1)  # 颜色通道提取
print(b)
img = cv2.merge((b, g, r))  # 颜色通道合并
print(img)
# show('img', img)
imgb = img.copy()  # 只保留B通道
imgb[:, :, 1] = 0
imgb[:, :, 2] = 0
# show('B', imgb)
cv2.destroyAllWindows()

'''
视频的读取
'''

'''
video = cv2.VideoCapture('test.mp4')
if video.isOpened():  # 检查读取是否正常
    opened, frame = video.read()  # frame现在是视频的第一帧，然后每执行一次cv.read()就再读取一帧
else:
    opened = False
while opened:
    ret, frame = video.read()
    if frame is None:
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将frame转换成灰度图gray
        cv2.imshow('result', gray)  # 展示灰度
        # cv2.imshow('result',frame)  # 展示彩色
        if cv2.waitKey(10) & 0xFF == 27:  # esc退出
            break

video.release()
cv2.destroyAllWindows()
'''

'''
自己写的视频读取
'''

vc = cv2.VideoCapture('zed1.avi')
if vc.isOpened():
    op = True
else:
    op = False

while op:
    ret, frame = vc.read()
    if frame is None:
        break
    cv2.imshow('result', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    # 这个if实现了按下esc键中断循环，位运算表示取waitkey方法返回值的后8位，避免了其他按键干扰
