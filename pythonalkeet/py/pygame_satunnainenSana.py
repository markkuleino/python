# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:58:26 2019

@author: MarkkuLeino
"""

from random import randrange
import pygame
#import time
import sys  #Fontin polkua varten!

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('matrix-efekti')

green = (0, 255, 0) 
black = (0, 0, 0)
screen.fill(black)

merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö"
sana = ''
for i in range(10):
    sana = sana + merkit[randrange(len(merkit))]
     
pygame.init()  #Tarvitaan ainakin fontteja varten
font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', 48)
text = font.render(sana , True, green, black)
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

pygame.display.flip()
screen.blit(text, textrect)
pygame.display.update()

running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          running = False

#time.sleep(3)
pygame.display.quit()
pygame.quit()
#sys.exit()