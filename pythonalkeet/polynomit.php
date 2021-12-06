<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Polynomilaskentaa</h3>


<p>Polynomit on elämän suola. Tietokoneelle polynomi voidaan kirjoittaa esim. <code>Px = 3*x^2 - 2*x +1</code> ja <code>Qx = -2*x^3 +x</code>. Lasketaan ne:</p>

<pre><code class="python">for x in range(3,10):
	Px = 3*x^2 - 2*x +1
	Qx = -2*x^3 +x

	print( f"P({x}) = {Px} \t \t Q({x}) = {Qx}" )
</code></pre>

<p>Käsky <code>range(3,10)</code> tekee listan luvuista 3, 4, 5, 6, 7, 8 ja 9. Silmukka <code>for</code> käy sen läpi. Tulostus eli <code>print()</code>-lause on mielenkiintoinen, mutta ei vaikea. Mieti sitä. Sana \t on tabulaattori eli sarkain.
</p>

<h3>Polynomin kuvaaja</h3>

<p>Polynomit ovat kivoja ja hauskan näköisiä. Piirretään polynomi <code>P(x) = -2x^3 - 2x^2 + 2x +2</code>. Käytetään hieman yksinkertaistettuja asioita, joten meidän tarvitsee antaa Pythonille ainoastaan tieto polynomin kertoimista asteen mukaisessa järjestyksessä (hahaa; näitä harjoiteltiin tunnilla &mdash; ei turhaan, siis). 



<div class="row">
<div class="six columns">
<img src="img/polynomiPoly1d.png"></img>
</div>
<div class = "six columns">
<p><code>numpy</code> on matemaattinen kirjasto ja <code>matplotlib</code> on tulostamiseen käytetty kirjasto.</p>
<p>Ensin määrätään <code>x</code>, eli sanotaan että se kulkee -2:sta 2:een yhteensä 50 pistettä. Funtkio <code>poly1d</code> laskee <code>y</code>:n arvot. Sitten se vain piirretään.</p> 

<?php img('img/polynomi_1d.png');?>

</div>
</div>



<h3>Pinnan piirtäminen</h3>

<p>Matikantunnilla joudumme jäämään 1-ulotteisiin kuvioihin, mutta täällä minä, Python, kontrolloin ja saan näyttää kaksiulotteisen funktion eli pinnan. Nyt tulostetaan <code>z</code>-suuntaan pinta, kun <code>x</code> ja <code>y</code> muuttuvat.




<div class="row">
<div class="six columns">
<pre><code>import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)
#F = 3 + 2*X + 4*X*Y + 5*X*X
F = X*X - Y*Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F)
plt.show()
</code></pre>
</div>
<div class = "six columns">
<?php img('img/polynomi_satulapiste.png');?>
</div>
</div>

<h3>Tehtäviä</h3>

<p class="tehtava">1. Laske polynomien <code>Px</code> ja <code>Qx</code> summa ja tulosta se.</p>

<p class="tehtava">2. Laske kirjan tehtäviä.</p>


<p class="tehtava">3. Kysy <code>x = input()</code>-käskyllä missä pisteessä polynomi lasketaan ja kerro vastaus.</p>

<p class="tehtava">4. Piirrä kuvaajia erilaista polynomeista. Yritä etsiä nollakohtia.</p>



<?php include('toc.php');?>

























<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
