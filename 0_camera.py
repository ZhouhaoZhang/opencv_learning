import cv2
import numpy as np

vc1 = cv2.VideoCapture(0)
vc2 = cv2.VideoCapture(1)

out = cv2.VideoWriter('result.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20,
                      (1920 * 2, 1080))
if vc1.isOpened():
    op = True
else:
    op = False

while op:
    ret1, frame1 = vc1.read()
    ret2, frame2 = vc2.read()
    if frame1 is None:
        break
    frame = np.hstack((frame1, frame2))
    cv2.imshow('result', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
