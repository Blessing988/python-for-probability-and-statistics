"""
Generating a geometric sequence
: Determining the probability of success in getting a head after n tosses
"""

import numpy as np
import matplotlib.pyplot as plt

p = 1/2
n = np.arange(0, 10)

X = np.power(p, n)

plt.bar(n, X)
plt.show()
