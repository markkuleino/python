# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:16:15 2019

@author: MarkkuLeino
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from scipy.interpolate import make_interp_spline#, BSpline


T = np.array([6, 7, 8, 9, 10, 11, 12])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])

xnew = np.linspace(T.min(), T.max(), 1000) 
spl = make_interp_spline(T, power, k=3)  # type: BSpline
ynew = spl(xnew)

fig, ax = plt.subplots()
line, = ax.plot(xnew, ynew, color='r')


def update( num, x, y, line):
    line.set_data( x[:num], y[:num])
    line.axes.axis([6, 10, 0, 1800])
    return line

ani = animation.FuncAnimation(fig, update, len(xnew),
                              fargs=[xnew, ynew, line],  
                              interval = 25, blit=True)

plt.plot(T,power)
plt.show()

#plt.plot(xnew, power_smooth)


# =============================================================================
# fig, ax = plt.subplots()
# line, = ax.plot(x, y, color='k')
# 
# def update(num, x, y, line):
#     line.set_data(x[:num], y[:num])
#     line.axes.axis([0, 10, 0, 1])
#     return line,
# 
# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
#                               interval=25, blit=True)
# #ani.save('test.gif')
# 
# 
# 
# =============================================================================
