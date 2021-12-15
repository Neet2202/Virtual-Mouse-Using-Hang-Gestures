#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
import pyautogui
import time


# In[ ]:


b_range = np.array([[88,78,20],[128,255,255]])
y_range = np.array([[21,70,80],[61,255,255]])
r_range = np.array([[158,85,72],[180 ,255,255]])


# In[ ]:


b_cen, y_pos, r_cen = [240,320],[240,320],[240,320]
cursor = [960,540]


# In[ ]:


area_r = [100,1700]
area_b = [100,1700]
area_y = [100,1700]

 


# In[ ]:


window = np.ones((7,7),np.uint8)


# In[ ]:


perform = False
showCentroid = False


# In[ ]:


def hsv_i(x):
    pass


# In[ ]:


def swap( array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


# In[ ]:


def distance( c1, c2):
    distance = pow( pow(c1[0]-c2[0],2) + pow(c1[1]-c2[1],2) , 0.5)
    return distance


# In[ ]:


def Status(key):
    global perform
    global showCentroid
    global y_range,r_range,b_range
    
    if key == ord('p'):
        perform = not perform
        if perform:
            print('Mouse simulation ON...')
        else:
            print('Mouse simulation OFF...')

    elif key == ord('c'):
        showCentroid = not showCentroid
        if showCentroid:
            print('Showing Centroids...')
        else:
            print('Not Showing Centroids...')

    elif key == ord('r'):
        print('**********************************************************************')
        print('	You have entered recalibration mode.')
        print(' Use the trackbars to calibrate and press SPACE when done.')
        print('	Press D to use the default settings')
        print('**********************************************************************')

        y_range = colorCalibration('Yellow',y_range)
        r_range = colorCalibration('Red', r_range)
        b_range = colorCalibration('Blue', b_range)
    
    else:
        pass


# In[ ]:


def createMask(hsv_frame, color_Range):
    
    mask = cv2.inRange( hsv_frame, color_Range[0], color_Range[1])
    eroded = cv2.erode( mask,window, iterations=1)
    dilated = cv2.dilate( eroded, window, iterations=1)
    
    return dilated


# In[ ]:


def findCentroid(vid, color_area, mask, showCentroid):
    
    contour, _ = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    l=len(contour)
    area = np.zeros(l)

   
    for i in range(l):
        if cv2.contourArea(contour[i])>color_area[0] and cv2.contourArea(contour[i])<color_area[1]:
            area[i] = cv2.contourArea(contour[i])
        else:
            area[i] = 0
    
    a = sorted( area, reverse=True)	

   
    for i in range(l):
        for j in range(1):
            if area[i] == a[j]:
                swap( contour, i, j)

    if l > 0 :
       
        M = cv2.moments(contour[0])
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            center = (cx,cy)
            if showCentroid:
                cv2.circle( vid, center, 5, (0,0,255), -1)
                    
            return center
    else:
        
        return (-1,-1)


# In[ ]:


def colorCalibration(color, def_range):
    
    global window
    calibrate_c = 'Calibrate '+ color
    cv2.namedWindow(calibrate_c)
    cv2.createTrackbar('Hue', calibrate_c, def_range[0][0]+20, 180, hsv_i)
    cv2.createTrackbar('Sat', calibrate_c, def_range[0][1]   , 255, hsv_i)
    cv2.createTrackbar('Val', calibrate_c, def_range[0][2]   , 255, hsv_i)
    while(1):
        ret , frameinv = cap.read()
        frame=cv2.flip(frameinv ,1)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hue = cv2.getTrackbarPos('Hue', calibrate_c)
        sat = cv2.getTrackbarPos('Sat', calibrate_c)
        val = cv2.getTrackbarPos('Val', calibrate_c)

        lower = np.array([hue-20,sat,val])
        upper = np.array([hue+20,255,255])

        mask = cv2.inRange(hsv, lower, upper)
        eroded = cv2.erode( mask, window, iterations=1)
        dilated = cv2.dilate( eroded, window, iterations=1)

        cv2.imshow(calibrate_c, dilated)

        k = cv2.waitKey(5) & 0xFF
        if k == ord(' '):
            cv2.destroyWindow(calibrate_c)
            return np.array([[hue-20,sat,val],[hue+20,255,255]])
        elif k == ord('d'):
            cv2.destroyWindow(calibrate_c)
            return def_range






# In[ ]:


def setCursorPos( yc, pyp):
    
    yp = np.zeros(2)
    
    if abs(yc[0]-pyp[0])<5 and abs(yc[1]-pyp[1])<5:
        yp[0] = yc[0] + .7*(pyp[0]-yc[0]) 
        yp[1] = yc[1] + .7*(pyp[1]-yc[1])
    else:
        yp[0] = yc[0] + .1*(pyp[0]-yc[0])
        yp[1] = yc[1] + .1*(pyp[1]-yc[1])
    
    return yp


# In[ ]:


def Action(yp, rc, bc):
    out = np.array(['move', 'false'])
    if rc[0]!=-1 and bc[0]!=-1:
        
        if distance(yp,rc)<50 and distance(yp,bc)<50 and distance(rc,bc)<50 :
            out[0] = 'drag'
            out[1] = 'true'
            return out
        elif distance(rc,bc)<40: 
            out[0] = 'left'
            return out
        elif distance(yp,rc)<40:
            out[0] = 'right'
            return out
        elif distance(yp,rc)>40 and rc[1]-bc[1]>120:
            out[0] = 'down'
            return out
        elif bc[1]-rc[1]>110:
            out[0] = 'up'
            return out
        else:
            return out

    else:
        out[0] = -1
        return out


# In[ ]:


def performAction( yp, rc, bc, action, drag, perform):
    if perform:
        cursor[0] = 4*(yp[0]-110)
        cursor[1] = 4*(yp[1]-120)
        if action == 'move':

            if yp[0]>110 and yp[0]<590 and yp[1]>120 and yp[1]<390:
                pyautogui.moveTo(cursor[0],cursor[1])
            elif yp[0]<110 and yp[1]>120 and yp[1]<390:
                pyautogui.moveTo( 8 , cursor[1])
            elif yp[0]>590 and yp[1]>120 and yp[1]<390:
                pyautogui.moveTo(1912, cursor[1])
            elif yp[0]>110 and yp[0]<590 and yp[1]<120:
                pyautogui.moveTo(cursor[0] , 8)
            elif yp[0]>110 and yp[0]<590 and yp[1]>390:
                pyautogui.moveTo(cursor[0] , 1072)
            elif yp[0]<110 and yp[1]<120:
                pyautogui.moveTo(8, 8)
            elif yp[0]<110 and yp[1]>390:
                pyautogui.moveTo(8, 1072)
            elif yp[0]>590 and yp[1]>390:
                pyautogui.moveTo(1912, 1072)
            else:
                pyautogui.moveTo(1912, 8)

        elif action == 'left':
            pyautogui.click(button = 'left')

        elif action == 'right':
            pyautogui.click(button = 'right')
            time.sleep(0.3)

        elif action == 'up':
            pyautogui.scroll(5)
            
        elif action == 'down':
            pyautogui.scroll(-5)
            

        elif action == 'drag' and drag == 'true':
            global y_pos
            drag = 'false'
            pyautogui.mouseDown()
        
            while(1):
                
                    k = cv2.waitKey(10) & 0xFF
                    Status(k)

                    _, frameinv = cap.read()
                
                    frame = cv2.flip( frameinv, 1)

                    hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)

                    b_mask = createMask( hsv, b_range)
                    r_mask = createMask( hsv, r_range)
                    y_mask = createMask( hsv, y_range)

                    py_pos = y_pos 

                    b_cen = findCentroid( frame, area_b, b_mask, showCentroid)
                    r_cen = findCentroid( frame, area_r, r_mask, showCentroid)	
                    y_cen = findCentroid( frame, area_y, y_mask, showCentroid)

                    if    py_pos[0]!=-1 and y_cen[0]!=-1:
                          y_pos = setCursorPos(y_cen, py_pos)

                    performAction(y_pos,r_cen, b_cen, 'move', drag, perform)
                    cv2.imshow('Frame', frame)

                    if distance(y_pos,r_cen)>60 or distance(y_pos,b_cen)>60 or distance(r_cen,b_cen)>60:
                            break

            pyautogui.mouseUp()


# In[ ]:


cap = cv2.VideoCapture(0)

print('**********************************************************************')
print('You have entered calibration mode.')
print('Use the trackbars to calibrate and press SPACE when done.')
print('Press D to use the default settings.')
print('**********************************************************************')

y_range = colorCalibration('Yellow', y_range)
r_range = colorCalibration('Red', r_range)
b_range = colorCalibration('Blue', b_range)
print('Calibration Successfull...')

cv2.namedWindow('Frame')

print('**********************************************************************')
print('Press P to turn ON and OFF mouse simulation.')
print('Press C to display the centroid of various colours.')
print('Press R to recalibrate color ranges.')
print('Press ESC to exit.')
print('**********************************************************************')
while(1):
        k = cv2.waitKey(10) & 0xFF
        Status(k)


        _, frameinv = cap.read()
      
        frame = cv2.flip( frameinv, 1)

        hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)

        b_mask = createMask( hsv, b_range)
        r_mask = createMask( hsv, r_range)
        y_mask = createMask( hsv, y_range)

        py_pos = y_pos 

        b_cen = findCentroid( frame, area_b, b_mask, showCentroid)
        r_cen = findCentroid( frame, area_r, r_mask, showCentroid)
        y_cen = findCentroid( frame, area_y, y_mask, showCentroid)
        if      py_pos[0]!=-1 and y_cen[0]!=-1 and y_pos[0]!=-1:
                y_pos = setCursorPos(y_cen, py_pos)
        output = Action(y_pos, r_cen, b_cen)
        if output[0]!=-1:
                performAction(y_pos, r_cen, b_cen, output[0], output[1], perform)

        cv2.imshow('Frame', frame)

        if k == 27:
            break

cv2.destroyAllWindows()


# In[ ]:



