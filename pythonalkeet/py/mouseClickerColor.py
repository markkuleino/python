import pyautogui
import cv2, numpy as np
import time

#https://mouseaccuracy.com/

ColorRGB = [100,0,22.7] #RGB 0...100
lowerRange = np.array([0, 100, 100])
upperRange = np.array([5, 255, 255])

time.sleep(1)

time_end = time.time() + 10
while time.time() < time_end:
                       
    image = pyautogui.screenshot()
    #Convert image to HSV
    
    #image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    hsv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2HSV)
    
    mask = cv2.inRange(hsv, lowerRange, upperRange)

    #print( time.time() )

    #print( np.shape(mask ))

    #cv2.imshow('img', image)
    #cv2.imshow('mask', mask)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    # click 
    #for pt in zip(*loc[::-1]): 
    #    #cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
    #    pyautogui.moveTo( pt[0], pt[1] )
    #    print( pt )
    #    #time.sleep(0.1)
    #    #pyautogui.click()
        
    #cv2.imshow('kuva', image)