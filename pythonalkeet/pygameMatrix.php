<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>PyGame &mdash; Matrix, putoavat kirjaimet</h1>




<p>Asenna <code>pygame</code> Anaconda prompt:lla, </p>
<pre><code>pip install pygame
</code></pre>


<p>Paljon ideoita: 
https://codegolf.stackexchange.com/questions/17285/make-the-matrix-digital-rain-using-the-shortest-amount-of-code
</p>
<ul>
<li>Unikoodi-merkistö</li>
<li>Pystyrivit vaalenevat kohti alaosaa</li>
<li>Pystyrivi saattaa loppua kesken, muista että vaalennus saisi olla oikein.</li>
<li>Satunnainen fontin koko jokaisella pystyrivillä</li>
<li>Tuuliefekti</li>
<li>Käyttäjän antama satunnaisluku tulee näkyviin keskelle</li>
<li>Äänet</li>
<li></li>

</ul>


<h3>PyGame: ensimmäinen ikkuna</h3>


<p>Avataan ruudulle <code>pygame</code>-ikkuna, johon voidaan piirtää kuvioita tai tekstiä. Kuvaruutu katoaa laittamalla hiiren päälle ja painamalla jotain näppäimistön nappia. </p>


<pre><code>
import pygame

(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('1. ikkuna')

background_colour = (255,255,255)
#background_colour = (0,0,0)
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          running = False

pygame.display.quit()
pygame.quit()
</code></pre>


<h3>Tekstiä ruudulla (ikkunassa)</h3>

<p>Windowssissa fontit löytyvät osoitteesta C:\Windows\Fonts ja sieltä voi kopioida fontin nimen käytettäväksi <code>pygame.font.Font()</code>-käskyyn. Lisää punaisella merkityt edelliseen ohjelmaasi, ja saat teskstiä ruudulle.</p>


<?php img('py/pygame_tekstiaRuudulla.png');?>

<p class="tehtava">Tehtävä 1. Muuta tekstiä: lähetä tervehdys opettajallesi.</p>

<p class="tehtava">Tehtävä 2. Muuta fonttia: Kirjoita tekstejä eri kirjasimilla.</p>


<h3>Satunnainen sana ruudulle</h3>

<p>Matrix-putoavassa tekstissä sanat ovat melko satunnaisia. Kokeillaan tulostaa ensin sellainen näkyviin. Määritetään ensin käytettävät merkit ja tehdään niistä satunnainen sana.</p>



<img src="img/matrixSana.png">

<p>Käskyllä <code>randrange</code> saat valittua merkkijonosta yhden merkin, joka seuraavassa <code>for</code> -silmukassa laitetaan sanan perään. Lopuksi on kommentoituna odotuslause. Se hämää, jos näppäintö painamalla suljet ikkunan, mutta se ei sammukaan.</p>

<?php img('py/pygame_satunnainenSana.png');?>

<p class="tehtava">Tehtävä 3. Tee satunnainen sana, jonka pituus on kaksinkertainen nykyiseen nähden.</p>

<p class="tehtava">Tehtävä 4. Muuta ikkunan kokoa kohdassa <code>(width, height)=</code>.</p>

<p class="tehtava">Tehtävä 5*. Tulosta kaksi riviä tekstiä.</p>

<p class="tehtava">Tehtävä 6. Käytä erikoismerkkejä, esim. "'#¤%&/) sanan muodostamiseen.</p>


<h3>Tippuva ja himmeneva sana</h3>

<p>Kuvakaappaus tippuvasta sanasta on hieman heikohko, mutta oikeasti sana tippuu alaspäin. Samalla sen väri haalenee. Tätä varten muodostetaan funktioita.</p>

<img src="img/matrixTippuvaSana.gif">

<div class="row">
<div class="eight columns">

<?php img('py/pygame_tippuvaSana.png');?>
</div>
<div class="four columns">

</div>
<p>Aluksi määritellään funktiot. Muodostetaan <code>def</code>-käskyillä kaksi eri funktiota.</p>
</div>


<pre><code>
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
</code></pre>


<h3>Eri väriset kirjaimet</h3>

<pre><code>from random import randrange, random
import pygame
import time
import sys  #Fontin polkua varten!
import math

def satSana(pituus):
    merkit = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖabcdefghijklmnopqrstuvwxyzåäö"
    sana = ''
    for i in range(pituus):
        sana = sana + merkit[randrange(len(merkit))]
    return sana

def teeRivi(sana, alku, nopeus):
    font = pygame.font.Font('C:/WINDOWS/Fonts/BERNHC.TTF', fontsize)
    text = font.render(sana, True, (0,alku/nopeus,0), black)
    return text

def renderoiSana(sana, alku, nopeus, y):
    for y in range(1,pystyriveja):
        i = 0
        x = 10
        time.sleep(0.1)
        for kirjain in sana:
            x = x+15
            #print( y*nopeus[i])
            screen.blit(teeRivi(kirjain, alku[i], nopeus[i]*(y)), (x,y*fontsize))
            i = i+1
        pygame.display.update()
    
def alustaNopeus():
    sana = satSana(15)
    #sana = "Hellurei kaikille"
    alku = []
    for i in range(len(sana)):
        alku.append(randrange(100,255))
    nopeus = []
    for i in range(len(sana)):
        nopeus.append(5*random()+1)
    return sana, alku, nopeus
    
    
fontsize = 30
pystyriveja = 10
(width, height) = (300, fontsize * pystyriveja )
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('matrix-efekti')

black = (0, 0, 0)
screen.fill(black)
        
pygame.init()  #Tarvitaan ainakin fontteja varten
sana, alku, nopeus = alustaNopeus()

pygame.display.flip()

running = True
y = -fontsize
while running:   
    renderoiSana(sana, alku, nopeus, y)
    sana, alku, nopeus =  alustaNopeus()

    time.sleep(0.1)
     
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          running = False

pygame.display.quit()
pygame.quit()
#sys.exit()

</code></pre>

<h3>Pystyrivit</h3>

<p>Muutetaan koodia siten, että eletään pystyrivi kerrallaan. Tällöin on (ehkä) helpompi aloittaa uudestaan ylhäältä, ja samalla kenties saadaan jokaisen nopeus erilaiseksi.</p>

<p>Toteutetaan homma tekemällä datamatriisi, joka sisältää tulostettavat tekstit lähes oikeissa paikoissa. Sen lisäksi tarvitaan nopeus- ja värilistat. Nopeus on ykkösen lähellä oleva luku, jolla saadaan pystyrivi laskeutumaan nopeammin tai hitaammin. Väri on tummuusaste, kuten edellä. Lopettamisehto tarvitaan lisäksi. Se voisi olla sama kaikille?</p>


<pre><code>

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

</code></pre>



<?php include('toc.php');?>

















<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
