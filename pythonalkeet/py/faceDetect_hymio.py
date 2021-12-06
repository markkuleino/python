# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:24:39 2019

@author: MarkkuLeino
"""

import cv2

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#haar_cascade_face = cv2.CascadeClassifier('haarcascade_eye.xml')


hymio = cv2.imread('naamahymio.png',-1)
hymio_g = cv2.cvtColor( hymio, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

while(True):
    #Lue kuva kamerasta
    ret, frame = cap.read()

    # Muutetaan harmaasävyksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Näytä ruudulla

    #Kasvontunnistus
    faces_rects = haar_cascade_face.detectMultiScale(gray, scaleFactor =1.2, minNeighbors = 5);
    print('Faces found: ', len(faces_rects))

    for (x,y,w,h) in faces_rects:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

        resized = cv2.resize(hymio_g, (w,h),interpolation = cv2.INTER_AREA)

        y1, y2 = y, y + resized.shape[0]
        x1, x2 = x, x + resized.shape[1]

        gray[y1:y2, x1:x2] = resized
        #cv2.addWeighted(gray, 0.4, hymio_g, 0.1, 0)

    
    sobel_x=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=1)
    sobel_y=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=1)
    cv2.imshow('sobelx',sobel_x)

    #cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lopetetaan
cap.release()
cv2.destroyAllWindows()
