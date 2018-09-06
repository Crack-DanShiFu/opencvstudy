import cv2
import numpy as np
import imutils
from PIL import Image

cap = cv2.VideoCapture(0)
firstFrame = None
num = 1
while (1):
    # get a frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)
    # 如果第一帧是None，对其进行初始化
    if firstFrame is None:
        firstFrame = gray
        continue
    # 计算当前帧和第一帧的不同
    frameDelta = cv2.absdiff(firstFrame, gray)
    # if num % 5 == 0:
    #     firstFrame = gray
    num += 1
    thresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=5)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    # 遍历轮廓
    for c in cnts:
        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
        # 计算轮廓的边界框，在当前帧中画出该框
        (x, y, w, h) = cv2.boundingRect(c)
        if w + h > 200:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            text = "Occupied"
            if num % 50 == 0:
                path = "C:/Users/Crack/Desktop/img/" + str(num) + ".png"
                framenew = frame[y:y + h,x:x + w]
                cv2.imwrite(path, framenew)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
