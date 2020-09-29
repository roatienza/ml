'''Utility for plotting a polynomial with 2 minima 
and its derivative
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.5, 3.0, 0.1)
c = [1, -1, -5, 0, 4]
d = [4, -3, -10, 0]
y = np.polyval(c, x)
z = np.polyval(d, x)
plt.xlabel(r'$\theta$')
plt.ylabel(r'$L\/\/\/and\/\/\/\frac{dL}{d\theta}$')
plt.plot(x, y, label=r'$L={\theta}^4 -{\theta}^3 -5{\theta}^2 +4$')
plt.plot(x, z, label=r'$\frac{dL}{d\theta},\/\/\/L_{min}\/\/\/at\/\/\/\theta=-1.25\/\/\/&\/\/\/2.0$')
plt.legend(loc=0)
plt.grid(b=True)
plt.savefig("double_min.png")
plt.show()
plt.close('all')
