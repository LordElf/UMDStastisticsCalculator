from math import *
import numpy as np

data = input()
data = data.replace(',', ' ')
data = data.split()
print(data)

#.23 32, 32.3 .2
data = np.array(data).astype(np.float)
data = np.sort(data)
sum = np.sum(data)
print(data)
print('sum: ', sum)
std = np.std(data)
print('std: ', std)