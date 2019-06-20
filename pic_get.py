import cv2
import time
def pic_get():
    
    cap = cv2.VideoCapture(1) 
    cap.set(3,1980)
    cap.set(4,1080)
    cap.set(10,20)
    cap.set(11,0)
    cap.set(12,50)
    cap.set(13,5)
    cap.set(15,103)
    i = 0
    message =  'Please set your camara in place, photo will be taken in 15 seconds, or you can press "q" to manual take it.'
    print(message)
    time.sleep(2)
    while(1):
        # get a frame 
        ret, frame = cap.read()
        # show a frame 
        cv2.imshow("capture", frame)
        if  cv2.waitKey(1) & 0xFF == ord('q') or i >= 900: 
            cv2.imwrite("/home/yangkehan/文档/project/image.jpg", frame)
            break
        i=i+1
    cap.release() 
    cv2.destroyAllWindows()

pic_get()
