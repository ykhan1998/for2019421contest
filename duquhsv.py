import cv2
 
# 读取图片并缩放方便显示
img = cv2.imread('image.jpg')

# BGR转化为HSV
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
# 鼠标点击响应事件
def getposHsv(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print("HSV is", HSV[y, x])

 
 
cv2.imshow("imageHSV", HSV)
cv2.imshow('image', img)
cv2.setMouseCallback("imageHSV", getposHsv)
cv2.waitKey(0)
