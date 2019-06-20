from collections import deque
import numpy as np
import imutils
import cv2  
import time
import pic_get as pg
import find_dot as fd
import find_car as fc
import scale as sc
import json
import cal

#initializing the arrays we need
dot_centers = [ ]
dot_radiuses = [ ]
car_center = [ ]
scal = [ ]
delta = [ ]
rad = [ ]
dis = [ ]
moves = [ ]

pg.pic_get()   #get the picture
fc.color_car(car_center)  #get the center pixel of the car
fd.color_dot(dot_centers, dot_radiuses)  #get the center pixel of dots
sc.basic_scal(scal)        #get the scale of the picture

if len(car_center) == 0:
    print('No car found, please retry')
    exit()
elif len(dot_centers) == 0:
    print('No dots found, please retry')
    exit()
else:
    #output the results
    x_car_center = car_center[0][0]   
    y_car_center = car_center[0][1]  
    p_x = scal[0]
    p_y = scal[1]

    #sort the result of dots' center and radius
    i = 0
    dots = [ ]
    while i<len(dot_centers):
        dots.append([dot_centers[i][0], dot_centers[i][1], dot_radiuses[i]])
        i = i+1
    dots.sort(key=lambda x:x[1], reverse=True)

    #get the real distance between dots and car in milimeter
    for dot in dots:
        sc.distance(p_x, p_y, x_car_center, y_car_center, dot[0], dot[1], delta)
        sc.lenthofradius(p_x, p_y, dot[2], rad)

    #sort the result of the real distance and radius
    results = [ ]
    j = 0
    while j<len(dis):
        dis[j].append(rad[j])
        if abs(dis[j][0])>599 or abs(dis[j][1])>815 or dis[j][2]>305 or dis[j][2]<5:
            del(dis[j])
            continue
        results.append(dis[j])
        #get the moves need to be take and delays of the move need to delay
        cal.distotime(dis[j], moves)
        j = j+1

    filename = 'moves.json'
    with open(filename, 'w') as f_obj:
        json.dump(moves, f_obj)
        #, indent=4
exit
        

