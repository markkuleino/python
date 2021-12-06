# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:11:04 2019

@author: MarkkuLeino
"""

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
#spl = make_interp_spline(xd, yd, k=3)  # type: BSpline
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








