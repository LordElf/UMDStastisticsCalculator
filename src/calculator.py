import numpy as np
from math import *

data = '415 420 422 423 425 429 432 434 437 439 445 446 448 451 459 463 464'
data = data.replace(',', ' ')
data = data.split()
print(data)

# .23 32, 32.3 .2
data = np.array(data).astype(np.float)
data = np.sort(data)
sum = np.sum(data)
print(data)
print('sum: ', sum)
n = len(data)
print('n = ', n)
mean = np.mean(data)
# t ditribution ddof = 1
stDev = np.std(data,ddof=0)
print('mean', mean)
print('stDev: ', stDev)

# normal distribution
print('normal')
# t alpha/2, n - 1
stDev = 3.1
mean = 24.0
n = 11
z = 2.228 
range = z * stDev / sqrt(n)
ciL = mean + range
ciS = mean - range
print('range: ', range)
print('CI: (', ciS, ciL, ')')

# prediction interval
range = z * stDev * sqrt(1+1/n)
print('prediction interval: (', mean - range, mean + range)

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
pBar = (pHat + z**2 / (2 * n)) / (1 + z**2 / n)
print('pHat: ', pHat, 'pBar', pBar)
CIRange = z * sqrt(pHat * (1 - pHat) / n + z**2/(4 * n**2)) / (1 + z**2/n)
print(CIRange)
print('CI : ', pBar - CIRange, pBar + CIRange)
