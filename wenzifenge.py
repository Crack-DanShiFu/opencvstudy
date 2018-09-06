import cv2
import imutils

# 1、读取图像，并把图像转换为灰度图像并显示
img = cv2.imread("13.png")  # 读取图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.dilate(thresh, None, iterations=1)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

# img_thre=thresh

#
# # 4、分割字符
# white = []  # 记录每一列的白色像素总和
# black = []  # ..........黑色.......
# height = img_thre.shape[0]
# width = img_thre.shape[1]
# white_max = 0
# black_max = 0
#
# # 计算每一列的黑白色像素总和
# for i in range(width):
#     s = 0  # 这一列白色总数
#     t = 0  # 这一列黑色总数
#     for j in range(height):
#         if img_thre[j][i] == 255:
#             s += 1
#         if img_thre[j][i] == 0:
#             t += 1
#     white_max = max(white_max, s)
#     black_max = max(black_max, t)
#     white.append(s)
#     black.append(t)
#     print(s)
#     print(t)


cv2.imshow('gray', img)  # 显示图片
cv2.waitKey(0)
