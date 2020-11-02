import numpy as np
from math import *

data1 = '.95  .86  .71  .72  .74'
data = '.71  .85  .62  .72  .64'
data2 = '.69  .68  .51  .73  .44'
delta = 0 
data = data.replace(',', ' ')
data = data.split()
data1 = data1.replace(',', ' ')
data1 = data1.split()
data2 = data2.replace(',', ' ')
data2 = data2.split()
data = np.array(data).astype(np.float)
data1 = np.array(data1).astype(np.float)
data2 = np.array(data2).astype(np.float)
print(data1)
print(data)
print(data2)

# chapter 10.1
# ANOVA table
x1d = np.sum(data1)
x2d = np.sum(data)
x3d = np.sum(data2)

mx1 = np.mean(data1)
mx2 = np.mean(data)
mx3 = np.mean(data2)

xdd = x1d + x2d + x3d
xdda = xdd / (3 * len(data))
print(xdda)

MSTr = (5/3-1) * ((mx1 - xdda)**2 + (mx2 - xdda)**2 + (mx3 - xdda)**2 )
print('MSTr: ', MSTr)
s1 = np.std(data1, ddof = 1)
s2 = np.std(data, ddof = 1)
s3 = np.std(data2, ddof = 1)
MSE = (s1**2 + s2**2 + s3**2) / 3
print('MSE: ', MSE)
F = MSTr / MSE
print('F: ', F)

# for pair data, assume that len(data) = len(data1)
# for i in range(0, len(data1)):
#     data[i] = data1[i] - data[i]

# .23 32, 32.3 .2
sum = np.sum(data)
print(data)
print('sum: ', sum)
n = len(data)
print('n = ', n)
mean = np.mean(data)
# t ditribution ddof = 1
stDev = np.std(data, ddof=1)
print('mean', mean)
print('stDev: ', stDev)

t = (mean - delta) / (stDev / sqrt(n))
print('t = ', t)

# normal distribution
print('normal')
# t(alpha/2, n - 1) t distribuyion ddof = 1
# stDev = 0.76 
# mean =8.42 
# n = 15 
z = 1.96
range = z * stDev / sqrt(n)
#range = z * stDev * sqrt(1+1/n)
ciL = mean + range
ciS = mean - range
print('range: ', range)
print('CI: (', ciS, ciL, ')')

# prediction interval
range = z * stDev * sqrt(1+1/n)
print('prediction interval: (', mean - range, mean + range)

# tolerance interval
k = 95
ci = 95
n = 5
# table A.6
tCritical = 5.079 
range = tCritical * stDev
print('tolerace interval', mean - range, mean + range)

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
