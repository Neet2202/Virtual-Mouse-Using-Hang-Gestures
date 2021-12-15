#!/usr/bin/env python
# coding: utf-8


import pyautogui

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







