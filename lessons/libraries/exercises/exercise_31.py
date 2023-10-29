import math
from time import perf_counter
import numpy as np
import scipy as sp

x = np.arange(0, math.pi / 2, .0001)
y = np.sin(x)
t1_start = perf_counter()
riemann_integral = np.sum(y * (math.pi / 2) / len(x))
t1_stop = perf_counter()
t1 = t1_stop - t1_start
t2_start = perf_counter()
result = sp.integrate.quad(lambda i: math.sin(i), 0, math.pi / 2)
scipy_integral = result[0]
t2_stop = perf_counter()
t2 = t2_stop - t2_start
print(t1)
print(t2)
