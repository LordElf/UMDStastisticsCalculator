from math import *
import numpy as np

data = "0	1	2	3	4	5	6	7	8	9	10"
freqcy = "2	4	8	12	9	6	6	-1	2	1	1"
data = data.replace(',', ' ')
data = data.split()
freqcy = freqcy.replace(',', ' ')
freqcy = freqcy.split()

data = np.array(data).astype(np.float)
freqcy = np.array(freqcy).astype(np.float)

sum = 0
for i in range (0, len(data)):
    sum += data[i] * freqcy[i]

n = np.sum(freqcy)
mean = sum / n
print('sum: ', sum)
print('n: ', n)
print('mean: ', mean)

z = 1.96

miuPre = mean + z**2 / (2 * n) 
buffer = z * (sqrt(z**2 + 4 * n * mean) / (2 * n))

print('miu = (', miuPre - buffer, miuPre + buffer)
