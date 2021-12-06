<?php include("preamble.php");?>


<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Python</h1>



<div class="docs-section">
<h3>Kilpikonnagrafiikkaa</h3>


<p>Kilpikonna piirtää viivaa kulkiessaan ruudulla. Kynän väriä voi vaihtaa ja sen voi nostaa ylös. Hauska epeli.</p>


<p>ikävä kyllä, Spyderin kanssa on pieniä ongelmia, mutta ei välitetä niistä. Koodit <a href="https://stackoverflow.com/questions/46102284/turtle-not-working-in-spyder-python-3-6">kannattanee</a> lopettaa aina käskyihin</p>
<pre><code>turtle.done()
turtle.bye() 
</code></pre>
<p>Asetuksista pitää muuttaa tools -> preferences -> IPython Console -> graphics muotoon <em>automatic</em>. Silti se ei ihan täysin toiminut, vaikka kuva tulee:</p>

<?php img('img/turtleVirhe.png');?>





<h3>Turtlen peruskäskyt</h3>

<p>Jo muutamalla <a href="https://docs.python.org/3.5/library/turtle.html">käskyllä</a> pääset alkuun: 
<code>forward()</code>, 
<code>backward()</code>, 
<code>right()</code>, 
<code>left()</code>, 
<code>setheading()</code>, 
<code>circle()</code>, 
<code>dot()</code>, 
<code>pendown()</code>, 
<code>penup()</code>, 
<code>pensize()</code> tai 
<code>color()</code>
</p>


<div class="row">
<div class="five columns">
<p>Kolmio:</p>
<pre><code class="python">from turtle import *

forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
done()
bye() 
</code></pre>
<p>Väritetty tähti:</p>
<pre><code class="python">from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
bye()
</code></pre>
<p></p>

</div>
<div class="five columns">
<p>Kolmio:</p>
<?php img('img/turtleKolmio.png');?>

<p>Väritetty tähti:</p>
<?php img('img/turtletahti.png');?>




</div>
</div>


<h3>Pari esimerkkiä lisää</h3>

	<div class="row">
<div class="five columns">
<p>Melkein nelikulmio:</p>
<pre><code class="python">from turtle import *
colors=['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = Pen()
bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
bye()
done()
</code></pre>
<p><a href="https://www.youtube.com/watch?v=BD5MTZ2nOH0">Ympyräiset</a>:</p>
<pre><code class="python">from turtle import *

bgcolor('black')
pensize = 5
for x in range(36):
    rt(90); pencolor("pink")
    circle(60,360)
    lt(120);pencolor("yellow")
    circle(90,360)
    lt(120); pencolor("aqua")
    circle(120,360)
    pencolor("red")
    circle(150)
bye()
done()
</code></pre>
<p></p>

</div>
<div class="five columns">
<p>Melkein nelikulmio:</p>
<?php img('img/turtleNelikulmio.png');?>

<p>Ympyräiset:</p>
<?php img('img/turtleCircle.png');?>




</div>
</div>

	
	
	
<h3>Tehtäviä</h3>


<p class="tehtava">Tehtävä 1. Piirrä talo.</p>

<p class="tehtava">Tehtava 2. Piirrä Mikki Hiiri.</p>

<p class="tehtava">Tehtava 3. Piirrä fraktaalipuu.</p>

<p class="tehtava">Tehtava 4. Katso <a href="https://duckduckgo.com/?q=python+turtle+graphics&iar=images&iax=images&ia=images">hakukoneesta</a> lisää piirrettävää ja vihjeitä..</p>



<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
