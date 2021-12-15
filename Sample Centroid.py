#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


cap= cv2.VideoCapture(0)


# In[3]:


import cv2
cap = cv2.VideoCapture(0)
while(1):
    
     # Capture frame-by-frame
    _, frameinv = cap.read()

    # flip horizontaly to get mirror image in camera
    frame = cv2.flip( frameinv, 1)
  
     # Our operations on the frame come here
    hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
	
     # Display the resulting frame
    cv2.imshow('Frame', hsv)
 
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:


# #*
# while(1):
    
#      # Capture frame
#     _, frameinv = cap.read()

#     frame = cv2.flip( frameinv, 1)
  
#     hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)

#      #resulting frame
#     cv2.imshow('Frame',b_mask)
 
#     k = cv2.waitKey(10) & 0xFF
#     if k == 27:
#         break
        
# cap.release()
# cv2.destroyAllWindows()


# In[ ]:


#create window
window= np.ones((7,7),np.uint8)


# In[ ]:


#specify color ranges
blue_range = np.array([[88,78,20],[128,255,255]])
yellow_range = np.array([[21,70,80],[61,255,255]])
red_range = np.array([[158,85,72],[180 ,255,255]])


# In[ ]:


#Remove noise
#filter out a particular color from the frame
def makeMask(hsv_frame, color_Range):
    
    mask = cv2.inRange( hsv_frame, color_Range[0], color_Range[1])

    eroded = cv2.erode( mask,window, iterations=1)
    
    dilated = cv2.dilate( eroded,window, iterations=1)
    
    return mask


# In[ ]:


#sample image
frameinv=cv2.imread("sample.JPEG")

frame = cv2.flip( frameinv, 1)
hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)


b_mask=makeMask(hsv,blue_range)

cv2.imshow("Frame",b_mask) #abstract blue one

cv2.waitKey(0)
cv2.destroyAllWindows() 


# In[ ]:


#blue area
b_area=[100,1700]


# In[ ]:


#swap valuea
def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp


# In[ ]:


contour, _ = cv2.findContours( b_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
l=len(contour)
area = np.zeros(l)
#filtering contours
for i in range(l):
    if cv2.contourArea(contour[i])>b_area[0] and cv2.contourArea(contour[i])<b_area[1]:
                
        area[i] = cv2.contourArea(contour[i])
    else:
        area[i] = 0
a = sorted( area, reverse=True)
#contours with largest valid area       
for i in range(l):
    for j in range(1):
        if area[i] == a[j]:
            swap( contour, i, j)


# In[ ]:


if l > 0 :
# finding centroid 

                M = cv2.moments(contour[0])
                if M['m00'] != 0:
            
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                        center = (cx,cy)
                        
                        if True:
                                cv2.circle( frame, center, 5, (0,0,255), -1) #create dot
                                
                        cv2.imshow('image',frame)
                        cv2.waitKey(0)


# In[ ]:


cx


# In[ ]:


cy


# In[ ]:


center=(cx,cy)


# In[ ]:


center


# In[ ]:


cv2.circle( frame, center, 5, (0,0,255), -1)


# In[ ]:





# In[ ]:




