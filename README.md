# Virtual mouse using hand gestures 🚀





```bash
It is a mouse simulation system which performs all the functions performed by your mouse corresponding to your hand movements
and gestures. Gesture recognition technique is used to interact with computers, such as interpreting sign language.We can move the 
cursor and perform a left-click, right-click, drag, select and scroll up and down. 
The predefined gestures make use of only three fingers marked by different colors. 
```




<b> CALIBRATION PHASE: </b> 
<br>
```bash
The purpose of the calibration phase is to allow the system to recognize the Hue Saturation Values of the colors chosen by the users, 
where it will store the values and settings The program acquires the frames that consist of input colors submitted by the users.


* Specify colors

* Create Trackbar 

* Get Trackbar position
```
![image](https://user-images.githubusercontent.com/78814611/146217662-57862e2b-900d-4f1d-b189-e8063664e458.png)

<b> NOISE FILTERATION PHASE: </b>
<br>
```bash
Due to noise captured by the webcam and vibrations in the hand, the centres keep vibrating around a mean position. 
To reduce the shakiness in cursor ,compare the new centre with the previous position of the cursor. 

* Video Mask

* Erosion

* Dilation
```
![image](https://user-images.githubusercontent.com/78814611/146217936-46e4ea40-f818-40da-a4dd-20dcb47438e4.png) ![image](https://user-images.githubusercontent.com/78814611/146217955-99fb6391-d4ff-4a43-aef5-b6d266e5b546.png)


<b> CONTOUR DETECTION PHASE: </b>
<br>
```bash
After image Filteration, the next step is to perform edge detection to obtain  the  hand  contour  in  the  image.  
Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity.

* Find Contour

* Find Centroid
```

![image](https://user-images.githubusercontent.com/78814611/146217699-3e7450c4-43fb-481e-be64-c59b99c71294.png)


<b> MOUSE ACTIONS: </b>
<br>
```bash
The program will executes the mouse actions based on the colours combinations exist in the processed frame for that 
three centres are sent for deciding what action needs to be performed depending on their relative positions. 

1.Free cursor movement
2.Right click 
3.Left Click 
4.Drag / Select 
5.Scroll up 
6.Scroll down
```

![image](https://user-images.githubusercontent.com/78814611/146217727-2cf3e28e-d6b2-4718-a359-91f309e61a0e.png) 

<b> For Left click / Right click: </b>
```bash
- Red and Blue colors are specified for left click option.Whenever Blue and Red color comes together,gesture is
recognized by the program further and it will perform action and after left click un-pinch the fingers and choose the next action

- Red and Yellow colors are specified for right click clicking the mouse. Whenever the Red and Yellow color comes
together  and the  gesture recognized by the program further and for next move un-pinch the fingers and choose the next action.
```
![image](https://user-images.githubusercontent.com/78814611/146217750-13e001ad-426d-4f57-93ce-e2488e68ba6b.png)



- <b> For scroll up / For scroll down : </b>
```bash
- To scroll up RED + BLUE color finger gesture is used..The scrolling takes place at the mouse cursor’s  current position.
- To scroll down RED + YELLOW color finger gesture is used.The final PyAutoGUI mouse function is scroll( ),
which will work passing an integer argument.The scrolling takes place at the mouse cursor’s current position. 
```
![image](https://user-images.githubusercontent.com/78814611/146217783-59fdedb3-a8cc-4def-b5a8-2781dc3fa163.png)
 
 
 
- <b> For drag: </b>
```bash
- Hold all colors together to drag anything.PyAutoGUI provides the pyautogui.dragTo( )
functions to drag the mouse cursor to a new location or a location relative to its current one.
```
![image](https://user-images.githubusercontent.com/78814611/146217818-f96d516f-38f4-4388-b930-525d8baa1969.png)
