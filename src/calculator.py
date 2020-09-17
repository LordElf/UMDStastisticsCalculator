import numpy as np
from math import *

data = "2.0	    1.1	    6.0	    1.6	5.4	0.4	    1.0	    5.3 15.8	0.7	4.8	0.9	    12.1	    5.3	0.6	" 
data = data.replace(',', ' ')
data = data.split()
print(data)

# .23 32, 32.3 .2
data = np.array(data).astype(np.float)
data = np.sort(data)
sum = np.sum(data)
print(data)
print('sum: ', sum)
print(len(data))
mean = np.mean(data)
stDev = np.std(data)
print('mean', mean)
print('stDev: ', stDev)

# normal distribution
print('normal')
z = 1.96
range = z * stDev / sqrt(len(data))
ciL = mean + range
ciS = mean - range
print('range: ', range)
print('CI: (', ciS, ciL, ')')

# chi disctribution
print('chi')
x1 = 46.979
x2 = 16.791
ciL = 2 * sum / x2
ciS = 2 * sum / x1
print('CI: (', ciS, ciL, ')')

# p hat
print('p hat')
z = 1.645
n = 149
pHat = 8 / n
pBar = (pHat + z**2 / n) / (1 + z**2 / n)
print('pHat: ', pHat, 'pBar', pBar)
CIRange = (z * sqrt(pHat * (1 - pHat) / 2 + z**2/(4 * n**2)) / (1 + z**2/n))
print('CI : ', pBar - CIRange, pBar + CIRange)
