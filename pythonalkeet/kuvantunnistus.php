<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Kuvan tunnistaminen kuvasta</h3>

<p>Etsitään kuvasta jokin toinen kuva. Helppoa, cv2:lla.</p>

<img src="py/kuvanetsiminenkuvasta.png">

<p>Se etsii <code>template</code>-nimisen kuvan <code>image</code>-nimisestä kuvasta käytännössä liu'uttamalla sitä <code>image</code>:n päällä. Lopuksi se palauttaa koordinaatit. </p>
<p>Numpy:n funktiolla <code>unravel</code> tulostetaan ne. Unravel on hieman erikoinen funktio. Alla on toinen, ehkä paremmin toimiva esimerkki.</p>


<p>Unravel:n ulostulon saa printattua helpolla:</p>
<pre><code>
for pt in np.unravel_index(result.argmax(), result.shape):
    print( pt )
</code></pre>
<p>mutta se on vähän monimutkainen;)</p>

<div class="row">
<div class="eight columns">

<pre><code>
import cv2
import numpy as np
import pyautogui


pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)


pyautogui.keyDown('winleft')
pyautogui.press('d')
pyautogui.keyUp('winleft')


#Lue ikonin kuva (etsittävä kuva)
template = cv2.imread('ikoni.png')
w, h, null = template.shape  #Sen koko. Tarvitaan laatikon piirtämisessä


result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


raja = 0.8
loc = np.where( result >=  raja )  

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2) 

cv2.imshow('kuva', image)


</code><pre>

</div>
<div class="four columns">
<p>Koodi näyttää työpöydän, ottaa kuvakaappauksen, vertaa sitä pikkukuvaan (template) ja etsii ne kohteet, joiden raja-arvo on suurempi kuin 0.8. Sen jälkeen se piirtää suorakaiteen löydettyjen ympärille ja vielä näyttää kuvan.</p>

</p>

<p>Alla on on toinen, joka toimivat joissain tapauksissa:, mutta ei aina koska se ei tarkista kuinka hyvin se vastasi alkuperäistä:</p>

<pre><code>
#Etsii suurimman ja pienimmän.
#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#top_left = max_loc
#bottom_right = (top_left[0] + w, top_left[1] + h)

#cv2.rectangle(image,top_left, bottom_right, 255, 2)

</code></pre>




</div>
</div>



<h3>Tehtäviä</h3>


<p class="tehtava">Etsi ikoni ruudulta.</P>


<p class="tehtava">Tuplaklikkaa ikonia aiemmilla opeillasi ja avaa ohjelma.</P>

<p class="tehtava">Etsi kaikki silmät kuvasta.</P>



<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
