<?php include("preamble.php");?>


<body style="">



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>

<h3>Asenna cv2</h3>

Anacondassa Open CV2 -kirjastoa ei ole, joten asennetaan se. Ensin avaa Anaconda prompt tai Anaconda Poweshell prompt:</p>

<img src="img/anacondaInstallNew.png">

<p>ja kirjoita siihen</p>
<pre><code>conda install -c menpo opencv
</code></pre>
<p>Nyt toimii.</p>


<div class="docs-section">
<h3>Kameran kuva ruudulle</h3>

Suoraan opencv:n <a href="https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html">tutoriaaleista</a>


<div class="row">
<div class="five columns">
<pre><code class="python">import cv2

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
</code></pre>

</div>
<div class="five columns">
<p>Kuva harmaasävyinä</p>



</div>
</div>


<h3>Kasvontunnistus openCV:lla</h3>

<p>Lataa muutama Haarin kaskadi nettisivulta:
<a href="https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV/tree/master/data/haarcascades">Haar cascades</a>. Eli lataa se xml-tiedosto, mikä ladataan Python-koodin alussa.


<div class="row">
<div class="seven columns">

<pre><code>import cv2

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    #Lue kuva kamerasta
    ret, frame = cap.read()

    # Muutetaan harmaasävyksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Kasvontunnistus
    faces_rects = haar_cascade_face.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5);
    print('Faces found: ', len(faces_rects))

	#Piirrä suorakaide
    for (x,y,w,h) in faces_rects:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lopetetaan
cap.release()
cv2.destroyAllWindows()</code></pre>
	
	
	
	
</div>
<div class="five columns">
<p>
<img class="u-full-width" src="img/kasvontunnistus.png">
</p>

<p>Aika helppoa, kuitenkin. Ohjeet löytyivät <a href="https://www.datacamp.com/community/tutorials/face-detection-python-opencv">Datacampin</a> sivuilta, mutta niitä on netti täynnä.</p>

<p>Haarin kaskaadit ovat mielenkiintoinen tapa etsiä kuvasta tunnistettavia piirteitä. <a href="https://vimeo.com/12774628">Videolta</a> voit katsoa, miten se toimii.</p>

</div>
</div>



<h3>Kasvonvaihto </h3>

<p>Vaihdetaan kameran löytämä naama alussa ladattuun <a href="py/naamahymio.png">kuvaan</a>. Huomaa, että älpinäkyyyttä eli alpha-kanavaa ei ole harmaasävykuvissa (määritelmän perusteella). Nyt ei leikitä väreillä, vaikka aika helppoa sekin olisi. Harjoitustehtävänä.</p>


<div class="row">
<div class="seven columns">

<pre><code>import cv2

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

hymio = cv2.imread('naamahymio.png',-1)
hymio_g = cv2.cvtColor( hymio, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)

while(True):
    #Lue kuva kamerasta
    ret, frame = cap.read()

    # Muutetaan harmaasävyksi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Kasvontunnistus
    faces_rects = haar_cascade_face.detectMultiScale(gray, scaleFactor =2.5, minNeighbors = 5);
    print('Faces found: ', len(faces_rects))

    for (x,y,w,h) in faces_rects:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

        resized = cv2.resize(hymio_g, (w,h),interpolation = cv2.INTER_AREA)

        y1, y2 = y, y + resized.shape[0]
        x1, x2 = x, x + resized.shape[1]

        gray[y1:y2, x1:x2] = resized
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lopetetaan
cap.release()
cv2.destroyAllWindows()
</code></pre>


</div>
<div class="five columns">
<img class="u-full-width" src="img/naama.gif">

<p>Käytetään <code>resize</code>-funktiota, joka interpoloi kuvan eri kokoiseksi. <code>Shape</code>-käsky ottaa kuvan koon ja <code>gray[y1:y2, x1:x2]</code> -komennolla talletetaan <code>resized</code>-kuva oikeaan paikkaan.

</p>



<p></p>

</div>
</div>
	
<h3>Tehtäviä</h3>

<p class="tehtava">Tehtävä 1. Käännä naamaa eri asentoihin. Kokeile käskyjä <code>gray = cv2.flip( gray, 0 )</code>, 
<code>gray = cv2.flip( gray, 1 )</code> ja
<code>gray = cv2.flip( gray, -1 )</code>

</p>

<p class="tehtava">Tehtävä 2. Tee kuvasta negatiivi. Mustavalkokuvassa pikselien arvot ovat välillä 0...1, joten vähennetään se ykkösestä. Lisää koodiin oikeaan paikkaan käsky <code>gray = 1 - gray</code> ja saat negativiin.


</p>



<p class="tehtava">Tehtävä 1. Tunnista silmä. Lataa koneellesi Haarin kaskadi silmälle aiemmin mainitusta sivustosta ja vaihda silmä-kaskaadi naaman tilalle. Muutin vielä scaleFactorya arvoon 2.5. Kokeile.</p>
 

<p class="tehtava">Tehtävä 2. Etsi kameran kuvasta reunat Sobelin algoritmilla:  
</p>
<pre><code>sobel_x=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
cv2.imshow('sobelx',sobel_x)
</code></pre>
<P>Muitakin algoritmeja löytyy. Kokeile etsiä niitä ja tutkia niitä.</p>

<p class="tehtava">Tehtava 3. Lisää kasvoihin piirretyt nenä ja korvat. </p>


<p class="tehtava">Tehtava 4. </p>



<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
