'''Utility for plotting a 2nd deg polynomial and
its derivative
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 2, 0.1)
c = [1, -1, -1]
d = [2, -1]
y = np.polyval(c, x)
z = np.polyval(d, x)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L\/\/\/and\/\/\/\frac{dL}{d\theta}$')
plt.plot(x, y, label=r'$L={\theta}^2 -\theta -1$')
plt.plot(x, z, label=r'$\frac{dL}{d\theta},\/\/\/\theta_{min}\/\/at\/\/\theta=0.5$')
plt.legend(loc=0)
plt.grid(b=True)
plt.savefig("parabola.png")
plt.show()
plt.close('all')
