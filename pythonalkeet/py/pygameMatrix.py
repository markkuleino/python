import pygame
import time
import sys  #Fontin polkua varten!
import numpy as np#Käytetään putoamisen laskemisessa.
#from random import choise
import random
import string
    
def rendaaMatriisi(M, X, Y, vari):
    #qprint('M = ')
    for i,j in np.ndindex(M.shape):
        if M[i,j].strip():
            #print( vari[j])
            #print( str( M[i,j]) +' (' +  str(X[i,j])+','+str(Y[i,j])+')')
            #text = font.render(M[i,j], True, (0,min(255, 255/((i+1)*vari[j])),0), black)
            text = font.render(M[i,j], True, (0,max(0,255-i*vari[j]),0), black)
            screen.blit( text, (X[i,j], Y[i,j]) )

        
def alustaNopeusKiihtyvyys(pituus):
    v = 45*np.random.rand(pituus)
    a = 5445*np.random.rand(pituus)

    return v, a
    
def laskeUusiPaikka(dt, x, v, a):
    x = x + dt*v + 0.5*a*dt*dt


    return x
    
def tarkistaSanat(S, x, y, fontsize, x0):
    ind = np.where( y[0,:] > 1)
    #print( ind )
     
    if len(ind) > 0:
        #Muutetaan Y:n, X:n ja S:n paikkaa yhdellä alaspäin
        x[1:, ind] = x[:-1, ind]
        x[0, ind] = x0[ind]
        y[1:, ind] = y[:-1, ind] 
        y[0, ind] = -fontsize + 1

        S[1:, ind] = S[:-1,ind]
        a = random.choice(string.ascii_letters + string.digits)
        
        
        S[0, ind] = np.full((1,len(ind)), a)

    return S, x, y


fontsize = 30
pystyriveja = 31

alkusana = np.array( list('Terve kaikille Matrix-faneille!'))
#alkusana = np.array( list('Ter'))
sanat = np.zeros( (pystyriveja, len(alkusana)), 'U1')
sanat[0,:] = alkusana


(width, height) = (fontsize*len(sanat[0]), fontsize * pystyriveja )
screen = pygame.display.set_mode((width, height))

X1 = (fontsize*0.95)*np.arange(0, len(sanat[0]))
X = np.repeat([X1], pystyriveja, 0)
Y = np.zeros( (pystyriveja, len(sanat[0])) ) 
vY, aY = alustaNopeusKiihtyvyys( len(sanat[0]) )
varikerroin = 8*(np.random.rand( len(alkusana) ) + 1 )

pygame.display.set_caption('matrix-efekti')

black = (0, 0, 0)
screen.fill(black)



pygame.init()  #Tarvitaan ainakin fontteja varten

font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', fontsize)

pygame.display.flip()

running = True
y = -fontsize
fps = 30
last_time = time.time()
while running:

    new_time = time.time()
    dt = new_time - last_time
    sleeptime = (1 - fps*dt/1000)/fps 
    if sleeptime > 0:
        time.sleep(sleeptime)
    last_time = new_time
    
    Y = laskeUusiPaikka(dt, Y, vY, aY)
    rendaaMatriisi(sanat, X, Y, varikerroin)
    pygame.display.update()
    
    sanat, X, Y = tarkistaSanat(sanat, X, Y, fontsize, X1)
    
    if np.random.rand()>0.99:
        vY, aY = alustaNopeusKiihtyvyys( len(sanat[0]) )

        
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          running = False




#time.sleep(3)
pygame.display.quit()
pygame.quit()
#sys.exit()


###
### FLL-pk-seudun aluekarsinnat vk 9.
### SYK:n kisa 5.2.2020
### SM-kisat joko vk 11 tai 12
###