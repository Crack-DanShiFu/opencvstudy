# 导入cv模块
import cv2

# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv2.imread("test.png", 0)
# 创建窗口并显示图像
new = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# new =cv2.flip(new,flipCode=-1)
rows, cols = new.shape[:2]
new = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
new = cv2.warpAffine(new, new, (cols, rows))
cv2.namedWindow("Image")
cv2.imshow("Image", new)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("imgnew.png", new)
# 释放窗口
cv2.destroyAllWindows()
