# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:40:02 2019

@author: MarkkuLeino
"""

import pygame
import sys  #Fontin polkua varten! Toimii joskus ilman tätä??

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('1. ikkuna')

white = (255, 255, 255) 
red = (255, 0, 0)
green = (0, 255, 0) 
blue = (0, 0, 128)

background_colour = green
screen.fill(background_colour)
pygame.init()  #Tarvitaan ainakin fontteja varten

font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', 48)
text = font.render('Hello World!', True, red, green)
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

pygame.display.quit()
pygame.quit()