<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Sanojen kuulustelupeli</h1>

<p>Koodi, mikä kyselee ruotsin (englannin, viron, venäjän?) sanat ja käskee sinun harjoitella lisää ja uudestaan.</p>

<p>Ensin pitää jaksaa kirjoittaa sanat:</p>
<pre><code>import random

sanat = [[ "auto", "car" ],
         [ "matto","carpet" ],
         [ "lemmikki","pet" ],
         [ "lehmä","cow" ],
         [ "paras","best" ],
         [ "lehmipoika","cowboy" ],
         [ "strutsi","struts" ],
         [ "Aura","Åbo" ],
         [ "tuuli","Wind" ]]
random.shuffle( sanat )  #Sekoitetaan ne
</code></pre>

<p>Käydään sanat läpi <code>for</code>-silmukassa, ja tarkistetaan, että onko sana sama:</p>
<img src="py/sanakuulustelu.png"></img>


<h2>Tehtäviä</h2>
<ol>

<li class="tehtava">Case insensitive. Tee koodista sellainen, että se ei välitä isoista tai suurista kirjaimista. Siispä, muuta kaikki isoiksi käskyllä <code>str.capitalize()</code>
</li>

<li class="tehtava">Uudestaan. Lisää koodiin kohta, jossa se kysyy, että haluatko uudestaan. Koodaa se toimivaksi.</li>

<li class="tehtava">Toisinpäin. Tee koodista sellainen, että sinun helppo (yhdestä koodin kohtaa) muuttaa se toimimaan toisinpäin, eli näyttää suomenkielisen sanan ja vaatii ulkomaankielistä sanaa.</li>


<?php include('toc.php');?>

















<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
