#!/usr/bin/env python
# coding: utf-8


import cv2
import numpy as np

def color(x):
    print(x)

#create window
img=np.zeros((300,512,3), np.uint8)

name = 'Calibrate'
cv2.namedWindow(name)

#createTrackbar

cv2.createTrackbar('Hue', name, 0, 255, color)
cv2.createTrackbar('Sat', name, 0, 255, color)
cv2.createTrackbar('Val', name, 0, 255, color)

#switchONandOFF
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch, name,0,1,color)

#show window
while(1):
    cv2.imshow(name, img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
        
    #get Trackbar position    
    hue = cv2.getTrackbarPos('Hue', name)
    sat = cv2.getTrackbarPos('Sat', name)
    val = cv2.getTrackbarPos('Val', name)
    s = cv2.getTrackbarPos(switch,name)

    if s == 0:
        img[:] = 0
    else:
        img[:] = [hue,sat,val]
cv2.destroyAllWindows()







