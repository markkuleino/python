<?php include("preamble.php");?>


<body style="">



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Animoi viivanpiirtoa</h1>

<h3>Tavoite</h3>

<img src="img/animationOptimized.gif">



<div class="docs-section">
<h3>Animointi ja viivan läheltä piirto</h3>



<div class="row">
<div class="seven columns">
<pre><code class="python">import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import make_interp_spline
from scipy.ndimage.filters import gaussian_filter1d #Smooth

xd = np.linspace(0, 11, 10)
yd = 10*np.random.random_sample(xd.shape)
ysmoothed = gaussian_filter1d(yd, sigma=.4)

x = np.linspace(0, 11, 1000)
spl = make_interp_spline(xd, ysmoothed, k=3)  # type: BSpline
y = spl(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='r')
lined, = ax.plot(xd, yd, color='r', marker='o', ls=' ' )

def update(num, x, y, line, xd,yd, lined):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 10])

    numd = np.sum( x[num] > xd ) + 2
    lined.set_data(xd[:numd], yd[:numd])
        
    return line, lined

ani = animation.FuncAnimation(fig, update, len(x), 
                              fargs=[x,y,line, xd,yd,lined],
                              interval=10, blit=True)
plt.show()
</code></pre>

</div>
<div class="five columns">
<p>Varsin suoraviivaista. <code>update</code>-funktio päivittää kuvaa, ja tässä se ottaa sisäänsä ne kaksi viivaa (joista toisessa on vain pisteet). </p>

<p>Gaussisella funktiolla <code>gaussian_filter1d</code> hieman smoothataan dataa, jotta viiva voidaan piirtää pisteiden läheltä. Filtteri on hyvin herkkä sigma-parametrin arvolle. </p>

<p>Pisteet <code>xd</code> ja <code>yd</code> sisältävät pisteet, joiden kautta muodostetaan 3:n asteen <a href="https://en.wikipedia.org/wiki/Spline_(mathematics)">splini</a> muuttujaan <code>y</code>. 

</div>
</div>

<h3>FFMpeg:n asentaminen &mdash; ei onnistunut</h3>

<p>
Ohjeet ovat <a href="https://stackoverflow.com/questions/13316397/matplotlib-animation-no-moviewriters-available#14574894">StackOverflow</a>ssa. Eli, downloadaa <a href="https://ffmpeg.zeranoe.com/builds/">paketti</a> ja jatka <a href="https://www.wikihow.com/Install-FFmpeg-on-Windows">Wikihow</a>n ohjeilla. Siellä pyydetään kopioimaan tiedostot juureen. Lisää bin-kansio polkuun. Environment variables löytyy Control Panel:n asetuksista (System) ja haulla. Sieltä kohta <pre>Path</pre> ja sinne pitää laittaa ajettavan (executable) polku. Ei auttanut. Ei toiminut.</p>

<p>Koska meillä on käytössä Anaconda, ffmpeg voidaan asentaa suoraan Anacondan shellistä käskyllä</p>
<pre><code>conda install -c conda-forge ffmpeg
</code></pre>
tai koska condassa saattaa olla uudempi/ vanhempi, myös 
<pre><code>conda install -c menpo ffmpeg
</code></pre>

<P>Ei toiminut tuokaan.</p>
<p>Ohjeen <a href="https://stackoverflow.com/questions/46997209/is-it-necessary-in-anaconda-for-matplotlib-to-install-ffmpeg-for-animation-savin">is it necessary in Anaconda for Matplotlib to install ffmpeg for animation saving?</a> metodeja en kokeillut.</p>

<h3>Tallentaminen gif:ksi</h3>

<p>Gif-animaatioksi sen kuvion sai talletettua helposti käskyllä (käytti PillowWriteriä)</p>
<pre><code>ani.save('animation.gif', writer='imagemagick', fps=50)
</code></pre>
<p>vaikka kone valittaa, että</p>
<pre>MovieWriter imagemagick unavailable; trying to use &lt;class 'matplotlib.animation.PillowWriter'&gt; instead.
</pre>
<p>Animaatiotiedosto on aika iso, mutta se pienenee esimerkiksi jollain netin optimointisoftalla.</p>

<h3>Tallentaminen png:iksi</h3>

<p>Lisää animaation päivitys-funktioon talletuskäsky, niin toimii:
<pre><code>
def update(num, x, y, line, xd,yd, lined):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 10])

    numd = np.sum( x[num] > xd ) + 2
    lined.set_data(xd[:numd], yd[:numd])
        
    plt.savefig("A" + str(num) + ".png")

    return line, lined
</code></pre>

<h3>Kuvan säätäminen</h3>
<p>Kuva pitää olla 4k-resoluutiota, ilman taustakuvaa ja aavistuksen läpinäkyvällä viivalla.</p>

<div class="row">
<div class="five columns">
<pre><code>
line, = ax.plot(x, y, color='r', alpha=0.7)
lined, = ax.plot(xd, yd, color='r', marker='o', ls=' ', alpha=0.7 )
</code></pre>
</div>
<div class="seven columns">
<p>Viivan läpinäkyvyys voidaan antaa piirtokäskyssä.</p>
</div>
</div>


<div class="row">
<div class="five columns">
<pre><code>
   plt.savefig("A" + str(num) + ".png", transparent = True)
</code></pre>
</div>
<div class="seven columns">
<p>Läpinäkyvä kuva saadaan käskemällä se läpinäkyväksi.</p>
</div>
</div>


<div class="row">
<div class="five columns">
<pre><code>
plt.figure(figsize=(4096, 2160), dpi=100)
</code></pre>

<pre><code>
	plt.savefig('myfig.png', dpi=1000)
</code></pre>



</div>
<div class="seven columns">
<p>Pythonin matplotlib haluaa kuvan mahtuvan ruudulle, joten 4k-resoluutioisen kuvan tulostaminen onkin hieman haastavampaa. Mutta se onnistuu dpi-parametrilla. Lisätietoja <a href="https://stackoverflow.com/questions/13714454/specifying-and-saving-a-figure-with-exact-size-in-pixels">StackOverflow:sta</a></p>
<p>Esimerkiksi, jos on <code>figsize=(7, 8), dpi=100</code> ja tulostetaan 100 dpi:llä, kuvan koko on 700&times;796 pikseliä. Jos tulostetaan 50 dpi:llä, saadaan kuvan kooksi 350&times;398 pikseliä eli puolet molempiin suuntiin.</p>

</div>
</div>

<p>Alla olevaan taulukkoon on koottu eri parametreillä tulostettuja kuvia. Viivan säädöt ovat vakiot; 
<code>lw = 30, markersize=100</code>. Jostain syystä ovat pikkaisen isot, mutta ei se mitään.</p>



<table class="u-full-width">
  <thead>
    <tr>
      <th>figsize</th>
      <th>dpi fig</th>
      <th>dpi save</th>
      <th>pixels</th>
      <th>image</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(10,10)</td>
      <td>10</td>
      <td>10</td>
      <td>148 &times 96</td>
      <td><a href="img/A21_10x10x10x10.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>30</td>
      <td>30</td>
      <td>300 &times 296</td>
      <td><a href="img/A21_10x10x30x30.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>100</td>
      <td>100</td>
      <td>1000 &times 982</td>
      <td><a href="img/A21_10x10x100x100.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>600</td>
      <td>600</td>
      <td>1924 &times 982</td>
      <td><a href="img/A21_10x10x600x600.png">kuva</a></td>
    </tr>
    <tr>
      <td>(20,20)</td>
      <td>600</td>
      <td>600</td>
      <td>1924 &times 982</td>
      <td><a href="img/A21_20x20x600x600.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>1200</td>
      <td>1200</td>
      <td>1924 &times 982</td>
      <td><a href="img/A21_10x10x1200x1200.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>600</td>
      <td>1200</td>
      <td>3848 &times 1964</td>
      <td><a href="img/A21_10x10x600x1200.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>1200</td>
      <td>7696 &times 3928</td>
      <td><a href="img/A21_10x10x300x1200.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>900</td>
      <td>5772 &times 2946</td>
      <td><a href="img/A21_10x10x300x900.png">kuva</a></td>
    </tr>
    <tr>
      <td>(8,8)</td>
      <td>300</td>
      <td>900</td>
      <td>5772 &times 2946</td>
      <td><a href="img/A21_8x8x300x900.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>800</td>
      <td>5130 &times 2618</td>
      <td><a href="img/A21_10x10x300x800.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>700</td>
      <td>4489 &times 2291</td>
      <td><a href="img/A21_10x10x300x700.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>650</td>
      <td>4168 &times 2127</td>
      <td><a href="img/A21_10x10x300x650.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>640</td>
      <td>4104 &times 2094</td>
      <td><a href="img/A21_10x10x300x640.png">kuva</a></td>
    </tr>
    <tr>
      <td>(10,10)</td>
      <td>300</td>
      <td>638</td>
      <td>4091 &times 2088</td>
      <td><a href="img/A21_10x10x300x638.png">kuva</a></td>
    </tr>
    <tr>
      <td>(5,5)</td>
      <td>300</td>
      <td>638</td>
      <td>3190 &times 2088</td>
      <td><a href="img/A21_5x5x300x638.png">kuva</a></td>
    </tr>



  </tbody>
</table>


<p>4K-<a href="https://en.wikipedia.org/wiki/4K_resolution">resoluutio</a> on noin 4096×2160 pikseliä, eli toiseksi alimmainen toimii hyvin.


<pre><code>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import make_interp_spline#, BSpline
from scipy.ndimage.filters import gaussian_filter1d #Smooth the datapoints
import matplotlib.patheffects as pe

xd = np.linspace(0, 11, 10)
yd = 10*np.random.random_sample(xd.shape)
ysmoothed = gaussian_filter1d(yd, sigma=.4)


x = np.linspace(0, 11, 100)
spl = make_interp_spline(xd, ysmoothed, k=3)  # type: BSpline
y = spl(x)

fig = plt.figure(figsize=(10,10), dpi=300)
ax = fig.add_axes( [0.1, 0.1, 0.8, 0.8],
                   ylim=(0, 10) )
line, = ax.plot(x, y, color='r', lw = 5, alpha=0.7)
lined, = ax.plot(xd, yd, color='r', marker='o', markersize=10, ls=' ', alpha=0.7 )

def update(num, x, y, line, xd,yd, lined):
    line.set_data(x[:num], y[:num])
    line.axes.axis([0, 10, 0, 10])

    numd = np.sum( x[num] > xd ) +2
    lined.set_data(xd[:numd], yd[:numd])
    
    plt.savefig("A\A" + str(num) + ".png", transparent = True, dpi=638)
            
    return line, lined

ani = animation.FuncAnimation(fig, update, len(x), 
                              fargs=[x,y,line, xd,yd,lined],
                              interval=10, blit=True)

#ani.save('animationframe.png', writer="imagemagick")

#writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#ani.save("movie.mp4", writer=writer)

plt.show()
</code></pre>





<h3>Tehtäviä</h3>

<p class="tehtava">Tehtävä 1.


</p>




<?php include('toc.php');?>




<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
