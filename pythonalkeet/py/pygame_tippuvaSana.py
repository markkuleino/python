# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:10:59 2019

@author: MarkkuLeino
"""

from random import randrange
import pygame
import time
import sys  #Fontin polkua varten!

def satSana(pituus):
    merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö"
    sana = ''
    for i in range(pituus):
        sana = sana + merkit[randrange(len(merkit))]
    return sana

def teeRivi(sana, rivi):
    font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', fontsize)
    text = font.render(sana, True, (0,255/rivi,0), black)
    return text

fontsize = 30
pystyriveja = 10
(width, height) = (300, fontsize * pystyriveja )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('matrix-efekti')

black = (0, 0, 0)
screen.fill(black)
    
sana = satSana(15)
pygame.init()  #Tarvitaan ainakin fontteja varten
text = teeRivi(sana, 2)

pygame.display.flip()
running = True
y = -fontsize
color = 1;
while running:
    screen.blit(teeRivi(sana, color), (0,y))
    pygame.display.update()
    time.sleep(0.1)
    y = y+fontsize
    if y > height:
        y=-fontsize
    color = color +1
    if color > 5:
        color = 1
          
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          running = False

#time.sleep(3)
pygame.display.quit()
pygame.quit()
#sys.exit()