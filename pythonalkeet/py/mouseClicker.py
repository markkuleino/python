import pyautogui
import cv2, numpy as np
import time

#https://mouseaccuracy.com/

target = cv2.imread("redBallTarget.png")
w, h, null = target.shape

time.sleep(1)

time_end = time.time() + 10
while time.time() < time_end:
                       
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(image, target, cv2.TM_CCOEFF_NORMED)

    raja = 0.8
    loc = np.where( result >=  raja )  

    print( time.time() )

    # click 
    for pt in zip(*loc[::-1]): 
        #cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 
        pyautogui.moveTo( pt[0], pt[1] )
        print( pt )
        #time.sleep(0.1)
        #pyautogui.click()
        
    #cv2.imshow('kuva', image)