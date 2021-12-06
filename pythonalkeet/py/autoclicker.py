# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:21:49 2019

@author: MarkkuLeino
"""

import cv2

cap = cv2.VideoCapture(0)

while(True):
    #Lue kuva kamerasta
    ret, frame = cap.read()

    # Muutetaan harmaasävyksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Näytä ruudulla
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lopetetaan
cap.release()
cv2.destroyAllWindows()