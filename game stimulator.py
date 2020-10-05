# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:09:06 2020

@author: Aditya Khandelwal
"""

import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
p1_x = 260
p1_y = 200

p2_x = 300
p2_y = 235

wc = cv2.VideoCapture(0)
    
# Read until video is completed
while(wc.isOpened()):
  # Capture frame-by-frame
  ret, img = wc.read()
  img = cv2.flip(img,1)
  if ret == True:
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 1)
        centre_new = [int((x + w + x)/2), int((y + h + y)/2)]
        
    cv2.rectangle(img, (p1_x, p1_y), (p2_x, p2_y), (255, 0, 0), 2)
    cv2.circle(img, (centre_new[0], centre_new[1]), 0, (0,0,255), 5)    
    
    if centre_new[0] > p1_x and centre_new[1] > p1_y and centre_new[0] < p2_x and centre_new[1] < p2_y:
        
        flag = 0
        
    if flag == 0 :
            
        if  centre_new[0] > p2_x : 
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print('RIGHT')
            flag = 1
            
        if  centre_new[0] < p1_x : 
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print('LEFT')
            flag = 1
        
        if  centre_new[1] < p1_y : 
            keyboard.press(Key.up)
            keyboard.release(Key.up)
            print('UP')
            flag = 1
            
        if  centre_new[1] > p2_y : 
            keyboard.press(Key.down)
            keyboard.release(Key.down)
            print('DOWN')
            flag = 1

    # Display the resulting frame
    cv2.imshow('Face',img)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  
  # Break the loop
  else: 
    break

# When everything done, release the video capture object
wc.release()
# Closes all the frames
cv2.destroyAllWindows()
