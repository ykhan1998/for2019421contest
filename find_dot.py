from collections import deque
import numpy as np
import imutils
import cv2  
import time
center_dot1 = [ ]
radius_dot1 = [ ]
def color_dot(center_dot, radius_dot):
    #设定红色阈值，HSV空间
    redLower = np.array([1, 45, 111])
    redUpper = np.array([10, 155, 180])
    #读取图片
    frame = cv2.imread('image.jpg')
    #转到HSV空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #根据阈值构建掩膜
    mask = cv2.inRange(hsv, redLower, redUpper)
    #腐蚀操作
    mask = cv2.erode(mask, None, iterations=2)
    #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
    mask = cv2.dilate(mask, None, iterations=2)
    #轮廓检测
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    #初始化瓶盖圆形轮廓质心
    center = None
    #如果存在轮廓
    if len(cnts) > 0:
        #找到面积最大的轮廓
        for c in cnts:
        #确定轮廓的外接圆
            ((x, y), radius) = cv2.minEnclosingCircle(c)
        #计算轮廓的矩
            M = cv2.moments(c)
        #计算质心
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            center_dot.append(center)
            radius_dot.append(radius)


