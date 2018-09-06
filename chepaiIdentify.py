import cv2
import imutils
import numpy as np

image = cv2.imread("chepai4.jpg")
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])
lower_yellow = np.array([15, 55, 55])
upper_yellow = np.array([50, 255, 255])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
output = cv2.bitwise_and(hsv, hsv, mask=mask_blue+mask_yellow)
# 根据阈值找到对应颜色
output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

Matrix = np.ones((20, 20), np.uint8)
img_edge1 = cv2.morphologyEx(output, cv2.MORPH_CLOSE, Matrix)
img_edge2 = cv2.morphologyEx(img_edge1, cv2.MORPH_OPEN, Matrix)

cnts = cv2.findContours(img_edge2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for c in cnts:
    # compute the bounding box for the contour, draw it on the frame,
    # and update the text
    # 计算轮廓的边界框，在当前帧中画出该框
    (x, y, w, h) = cv2.boundingRect(c)
    if w + h > 200:
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.drawContours(image, [c], -1, (0, 255, 0), 3)


cv2.imshow("chepai", image)

cv2.waitKey(0)
