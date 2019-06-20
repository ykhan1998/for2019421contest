from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
def basic_scal(scal):
    image = cv2.imread('image.jpg')
    blueLower = np.array([100, 43, 46])
    blueUpper = np.array([124, 255, 255])
    frame = cv2.imread('image.jpg')
    #转到HSV空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #根据阈值构建掩膜
    mask = cv2.inRange(hsv, blueLower, blueUpper)
    #腐蚀操作
    mask = cv2.erode(mask, None, iterations=2)
    #膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
    mask = cv2.dilate(mask, None, iterations=2)
    #轮廓检测
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  
    pixelsPerMetric_x = None
    pixelsPerMetric_y = None
    c = max(cnts, key = cv2.contourArea)
    orig = image.copy()
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="int")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl, br)
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr, br)
    dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
    if pixelsPerMetric_x is None:
        pixelsPerMetric_x = dB/220
    scal.append(pixelsPerMetric_x)
    if pixelsPerMetric_y is None:
        pixelsPerMetric_y = dA/270
    scal.append(pixelsPerMetric_y)
def distance(pixelsPerMetric_x, pixelsPerMetric_y, x1, y1, x2, y2, dis):
    dis_x = (x2-x1)/pixelsPerMetric_x
    dis_y = (y2-y1)/pixelsPerMetric_y
    dis.append([dis_x, dis_y])
def lenthofradius(pixelsPerMetric_x, pixelsPerMetric_y, radius, rad):
    if pixelsPerMetric_x >= pixelsPerMetric_y:
        rad.append(radius/pixelsPerMetric_y)
    else:
        rad.append(radius/pixelsPerMetric_x)
