# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:24:39 2019

@author: MarkkuLeino
"""

import cv2

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#haar_cascade_face = cv2.CascadeClassifier('haarcascade_eye.xml')


cap = cv2.VideoCapture(0)

while(True):
    #Lue kuva kamerasta
    ret, frame = cap.read()

    # Muutetaan harmaasävyksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Näytä ruudulla

    #Kasvontunnistus
    faces_rects = haar_cascade_face.detectMultiScale(gray, scaleFactor =2.5, minNeighbors = 5);
    print('Faces found: ', len(faces_rects))


    for (x,y,w,h) in faces_rects:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lopetetaan
cap.release()
cv2.destroyAllWindows()
