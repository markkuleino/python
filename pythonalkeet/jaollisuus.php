<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Kokonaislukujen jaollisuus ja alkuluvut</h3>


<p>Jaollisuussäännöt löytyvät kirjasta tai vaikka <a href="https://fi.wikipedia.org/wiki/Jaollisuus">Wikipediasta</a> tai <a href="http://www.luntti.net/ylakoulu/jaollisuus_saannot.php">Luntista</a>.</p>

</p>

<p>Python osaa laskea <a href="https://docs.python.org/3.5/library/operator.html#operator.mod">jakojäännöksen</a> hyvin helposti. Esimerkiksi 10/5 antaa jakojäännöseksii luvun 0, koska 5 jakaa kympin. Mutta 10/6 antaa jakojäännökseksi luvun 4, koska kuusi (6) ei mahdu kuin yhden kerran kymppiin, mutta yli jää 4. </p>





<h3>Selvitä luvun parillisuus</h3>

<p>Tehdään pieni koodinpätkä, joka kertoo onko annettu luku parillinen vai pariton.</p>


<div class="row">
<div class="five columns">

<pre><code class="python">i = int(input("Kerro luku: "))
if i % 2 == 0:
    print(" - parillinen")
else:
    print(" - pariton")
</code></pre>

<p  class="tehtava">Tehtävä 1. Muokkaa koodinpätkää selvittämään, onko luku jaollinen kolmella.</p>

</div>
<div class="five columns">
<p>Ensin kysytään luku ja muutetaan se <code>int()</code>-käskyllä kokonaisluvuksi. Kokeile poistaa <code>int</code>-käsky ja testaa toimiiko koodi silloin.</p>

<p>lasketaan jakojäännös kahdella (eli onko se parillinen). Jos jakojäännön on nolla <code>if i % 2 == 0:</code>, tulostetaan että parillinen. Muutoin (<code>else:</code>) <em>pariton</em>.</p>





</div>
</div>


<h3>Pienten lukujen parillisuus</h3>

<p>Muokataan äskeistä koodia kertomaan lukujen 1...10 <a href="https://courses.cs.ut.ee/MTAT.03.100/2012_fall/uploads/opik/03_liitlaused.html#tsukli-ja-tingimuslause-kombineerimine">parillisuus</a>.


<div class="row">
<div class="five columns">

<pre><code class="python">i = 1

while i <= 10:
    print("Luku: ", i)
    if i % 2 == 0:
        print(" - parillinen")
    else:
        print(" - pariton")
	i += 1
</code></pre>

<p class="tehtava">Tehtävä 2. Muokkaa koodinpätkää kertomaan kaikkien 100 pienempien lukujen jaollisuus!</p>

<p class="tehtava">Tehtävä 3. Selvitä, mitkä luvut, jotka ovat pienempiä kuin 100 ovat jaollisia seitsemällä.</p>

<p>Seitsemällä jaollisuus hypättiin matikan tunnilla yli, mutta täällä sekin voidaan käydä. On aluksi yllättävää, että <a href="https://www.easycalculation.com/divisibility-rule-by-7.php">näinkin helposti</a> voi sen testata. Siis kerrot luvun viimeisen numeron kahdella ja vähennät sen loppujen numeroiden muodostamasta luvusta. Tutki sen jaollisuutta seitsemällä vaikka samalla tavalla. </p>

<p class="tehtava">Tehtävä 4. Muuta koodia aloittamaan laskenta luvusta 314 kohti nollaa ja selvitä mitkä luvut ovat jaollisia luvulla 13.</p>


</div>
<div class="five columns">
<p>Äskeinen ehtolausekehärpäke laitetaan <em>silmukan</em> sisään. Silmukka on nyt <code>while 1 <= 10:</code> tyyppiä, eli sen sisässä olevaa toistetaan niin kauan kuin <code>i</code> on pienempi tai yhtäsuuri kuin kymmenen.</p>

<p>Nyt se tulostaa useamman luvun kerrasta.</p>



</div>
</div>



<h3>Alkuluvut</h3>

<p>Alkuluvut ovat lukuja, jotka ovat jaollisia vain luvulla 1 ja luvulla itsellään. Siis esimerkiksi luku 6=2&times;3 ei ole alkuluku, mutta luku 3 on alkuluku.</p>

<p>Tehdään lyhyt (ja tehoton) Python-skripti selvittämään, onko annettu luku alkuluku.</p>




<div class="row">
<div class="seven columns">

<pre><code class="python">i = int(input("Anna tutkittava luku: "))

if i % 2 == 0:
	print("Ei alkuluku - parillinen")
else:
	j = 3
	while j * j <= i:
		if i % j == 0:
			print("Jaollinen luvulla " + str(j) )
		j += 2
</code></pre>


<p class="tehtava">Tehtävä 5. Poista käskystä <code>str(j)</code> funktio <code>str</code> ja tutki, mitä tapahtuu.</p>

<p class="tehtava">Tehtävä 6. Lisää tulostukseen myös se toinen tulon tekijä, esimerkiksi <code>Luku 15 = 3 x 5</code>. </p>


</div>
<div class="five columns">
<P>Parillinen luku ei voi olla alkuluku.</p>

<p>Testataan silmukassa kaikilla parittomilla luvuilla, jos jakojäännös olisi nolla. Riittää kuitenkin tutkia vain luvut, joiden neliö on pienempi kuin tutkittava luku (<em>miksi?</em>). Jos jakojäännös on nolla, kerrotaan että se ei ole alkuluku, vaan jaollinen jollain luvulla.</p>

</div>
</div>


	
	
<h3>Tehtäviä</h3>


<p class="tehtava">Tehtävä 7. Selvitä <code>while</code>-silmukassa kaikki lukua 1000 pienemmät alkuluvut. </p>

<p class="tehtava">Tehtava 8. Muuta alkulukukoodia sellaiseksi, että sanoo <code>Alkuluku</code>, jos luku on alkuluku.</p>




<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
