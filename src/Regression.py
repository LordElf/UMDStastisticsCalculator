from math import *
import numpy as np

x = '3 3 4 5 6 6 7 8 8 9'
y = '9 5 12 9 14 16 22 18 24 22'
x = np.array(x.replace(',', ' ').split()).astype(np.float)
y = np.array(y.replace(',', ' ').split()).astype(np.float)
Sumx = np.sum(x)
Sumy = np.sum(y)
Sumxy = np.sum(x*y)
Sxy = Sumxy - Sumx * Sumy / len(x)
xMean = np.mean(x)
yMean = np.mean(y)
Sxx = np.sum((x - xMean)**2)
Syy = np.sum((y - yMean)**2)
Beta1 = Sxy/Sxx
Beta0 = yMean - Beta1 * xMean 
Beta1 = round(Beta1, 4)
Beta0 = round(Beta0, 4)
SST = Syy
print(SST)
SSE = Syy - Beta1 * Sxy
print('SSE', SSE)
r2 = 1 - SSE / SST
s = sqrt(SSE / (len(x) - 2))
print('s', s) 
print('r^2', r2)

print(f'Sumx = {Sumx}\nSumy = {Sumy}\nSumxy = {Sumxy}\nSxy = {Sxy} Sxx = {Sxx} Syy = {Syy}\nBeta1 = {Beta1} yMean = {yMean} xMean = {xMean} Beta0 = {Beta0}\n y = {Beta0} + {Beta1}x')

# Beta1 +- t(alpha/2, n-2)*(s/sqrt(Sxx))
t = 2.7408
range = t * s / sqrt(Sxx)
print(f'CI for Beta1: ({Beta1 - range}, {Beta1 + range})')