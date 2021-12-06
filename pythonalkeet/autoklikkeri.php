<?php include("preamble.php");?>


<body style="">



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Autoklikkeri</h3>


<p>Monta eri tapaa, mutta nyt käytetään <a href="https://pypi.org/project/PyAutoGUI/">pyAutoGUI</a>-menetelmää. Se toimii monessa eri ympäristössä. Anacondassa sitä ei ollut, joten asennetaan se. Ensin avaa Anaconda prompt tai Anaconda Poweshell prompt:</p>

<img src="img/anacondaInstallNew.png">

<p>ja kirjoita siihen</p>
<pre><code>conda install -c conda-forge pyautogui
</code></pre>
<p>Nyt toimii.</p>




<h3>Siirrä kursori</h3>



<div class="row">
<div class="five columns">
<p>Kolmio:</p>
<pre><code class="python">import pyautogui
pyautogui.click(100, 100)
</code></pre>

</div>
<div class="five columns">
<p>Klikkaa hiirellä kohtaa (100,100)</p>



</div>
</div>


<h3>Avaa ja kirjoita</h3>

	
<p>Nollakohta on vasen yläkulma, joten vasen alakulma poikkeaa monitorista riippuen. Siksi ensin luetaan ruudun koko:</p>
<pre><code class="python">import pyautogui
import time

w,h = pyautogui.size()
time.sleep(1)
pyautogui.moveTo(90, h)
pyautogui.click()
pyautogui.moveTo(128, h-70)
pyautogui.click()
pyautogui.write('Notepad', interval=0.25)
pyautogui.press('return')

#pyautogui.write('Moi kaikille!', interval=0.25)
#while True:
#    print( pyautogui.position() )

</code></pre>


	
	
<h3>Tehtäviä</h3>


<p class="tehtava">Tehtävä 1. </p>

<p class="tehtava">Tehtava 2. </p>

<p class="tehtava">Tehtava 3. .</p>

<p class="tehtava">Tehtava 4. </p>



<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
