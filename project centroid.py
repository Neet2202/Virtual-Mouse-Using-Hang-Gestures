#!/usr/bin/env python
# coding: utf-8

# In[4]:


def changeStatus(key):
    global perform
    global showCentroid
    global yellow_range,red_range,blue_range
    # toggle mouse simulation
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

            yellow_range = calibrateColor('Yellow', yellow_range)
            red_range = calibrateColor('Red', red_range)
            blue_range = calibrateColor('Blue', blue_range)
    else:
            pass

# cv2.inRange function is used to filter out a particular color from the frame
# The result then undergoes morphosis i.e. erosion and dilation
# Resultant frame is returned as mask 


# In[5]:


def drawCentroid(vid, color_area, mask, showCentroid):

        contour, _ = cv2.findContours( mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        l=len(contour)
        area = np.zeros(l)

# filtering contours on the basis of area rane specified globally 
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
# finding centroid using method of 'moments'
                M = cv2.moments(contour[0])
                if M['m00'] != 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                        center = (cx,cy)
                        if showCentroid:
                                cv2.circle( vid, center, 5, (0,0,255), -1)
                                
                        return center
        else:
# return error handling values
                    return (-1,-1)


# In[ ]:




