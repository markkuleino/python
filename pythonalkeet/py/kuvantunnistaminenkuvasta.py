# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:00:27 2019

@author: MarkkuLeino
"""

import cv2
import numpy as np
import pyautogui


pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')


#Lue ikonin kuva (etsittävä kuva)
template = cv2.imread('ikoni.png')
w, h, null = template.shape  #Sen koko. Tarvitaan laatikon piirtämisessä


result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


raja = 0.8
loc = np.where( result >=  raja )  

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

cv2.imshow('kuva', image)



#Etsii suurimman ja pienimmän.
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


#top_left = max_loc
#bottom_right = (top_left[0] + w, top_left[1] + h)

#cv2.rectangle(image,top_left, bottom_right, 255, 2)

#for pt in np.unravel_index(result.argmax(), result.shape):
#    print( pt )
    
    
#print( result.argmax() )
#print( result.shape )

