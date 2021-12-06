<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Asenna Python-ohjelmointiympäristö</h3>


<p>Käytämme <a href="https://www.anaconda.com/distribution/">Anaconda-versiota</a> Pythonista. Muutkin luultavasti toimivat lähes samalla tavalla. Sovelluskehittemenä käytämme <a href="https://www.spyder-ide.org">Spyder-ohjelmaa</a>, koska sekin on joku eläin ja tulee Anacondan mukana.</p>

<p>Asentaminen saattaa kestää hetken &mdash; huomaa että lataat oikean version. </p>


<h3>Hello World</h3>

<p>Ohjelmointi kuuluu aloittaa lähettämällä terveiset <a href="https://en.wikipedia.org/wiki/%22Hello,_World!%22_program">maailmalle</a>. Kirjoita seuraavat rivit Spyderiin, tallenna ja paina Play-nappia:

<div class="row">
<div class="four columns">

<pre><code class="python">print("Hello World")
</code></pre>

<p>Viereiselle ruudulle pitäisi ilmaantua teksti "Hello World". Jos ei tule, kysy opelta apua tai selvitä itse syy.</p>

</div>
<div class="eight columns">

<?php img('img/spyderAlkeet.png');?>


</div>
</div>

<h3>Tehtäviä</h3>

<ol>

<li  class="tehtava">Tee ohjelma, joka tulostaa ruudulle Eino Leinon runon <a href="https://www.kainuuneinoleinoseura.fi/">Nocturne</a>. Riviä voit jatkaa toiselle riville takakenolla \ ja rivinvaihdon saat \n-merkillä.</li>


<li  class="tehtava">Tee ohjelma, mikä tulostaa ruudulle alla olevan <a href="https://courses.cs.ut.ee/MTAT.03.100/2012_fall/uploads/opik/02_lihtlaused.html">tekstin</a>:

<?php img('img/AsciigameOver.png');?>
</li>


<li  class="tehtava">Lisää hyviä tulostettavia tekstejä löytyy hakusanalla <a href="https://duckduckgo.com/?q=ascii+art+&iar=images&iax=images&ia=images">ascii art</a>.</li>


<li  class="tehtava">Käskyllä <code>print( "X"*20 )</code> voit tulostaa 20 <code>X</code>-merkkiä. Tulosta ruutu täyteen "Y"-kirjaimia.</li>

<li  class="tehtava">Tietokoneesta tulostettavia perusmerkkejä kutsutaan ASCIIksi. Tutki <a href="http://ascii-table.com/ascii-extended-pc-list.php">extended ASCII -taulukkoa</a> ja tulosta alla olevan näköinen ruudukko tai käytä extended ascii -merkistöjä:

<?php img('img/AsciiExtendedBox.png');?>
</li>

<li  class="tehtava">Värejä voi tulostaa esim. <a href="https://pypi.org/project/colorama/">colorama</a>-paketilla_:
<pre><code>from colorama import Fore, Back, Style 
print(Fore.RED + 'Punainen on iloinen') 
print(Back.RED + 'Vihreä on vihreä') 
print(Style.DIM + 'Haalea?') 
print(Style.RESET_ALL) 
print('Normaali') 
</code></pre>
</li  class="tehtava">


<li  class="tehtava">Extended Ascii -merkistöllä tulosta alla olevan näköinen teksti:

<?php img('img/AsciiExtendedBox2.png');?>
</li>

<li  class="tehtava">Laajenna edellistä <code>for</code>-käskyllä eli käytä silmukkaa toistaaksesi tyhjää riviä:
<pre><code>for i in range(20):
    print("║" + " "*30 + "║")
</code></pre>

<?php img('img/AsciiExtendedBoxFor.png');?>
</li>


<li  class="tehtava">Käskyllä <code>nimi = input("Mikä on sinun nimesi")</code> voit kysyä kesken ohjelman suoritusta käyttäjän nimen. Tee ohjelma, mikä kysyy käyttäjän nimen ja tulostaa ruudulle tekstin <code>Moro, Markku</code>, jos käyttäjän nimi on Markku. Tulostuksessa voit yhdistää tekstin <code>+</code>-käskyllä. Vihje <a href="https://courses.cs.ut.ee/MTAT.03.100/2012_fall/uploads/opik/02_lihtlaused.html#milleks-muutujad">Tarton yu:n sivuilla lisää esimerkkejä</li>.

</ol>

<?php include('toc.php');?>

























<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
