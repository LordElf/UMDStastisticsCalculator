import numpy as np
from math import *
def info():
    choice = input("Setlect type of data set\n 1. normal 2.chi \n")
    data = input("Input dataset : \n")
    data = data.split()
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
    if (choice == "1"):
        run_normal(data)
    elif (choice == "2"):
        run_chi(data)
    else:
        run_normal(data)


# .23 32, 32.3 .2
# normal distribution
def run_normal(data):
    print('normal')
    z = input("look up z value: \n")
    z= float(z)
    stDev = np.std(data)
    mean = np.mean(data)
    range = z * stDev / sqrt(len(data))
    ciL = mean + range
    ciS = mean - range
    print('range: ', range)
    print('CI: (', ciS, ciL, ')')

# chi disctribution
def run_chi(data):
    print('chi')
    x1 = input(f"look up chi with v= {len(data)*2}\n x1:")
    x2 = input("and x2:\n")
    x1 = float(x1)
    x2 = float(x2)
    sum = np.sum(data)
    ciL = 2 * sum / x2
    ciS = 2 * sum / x1
    print('CI: (', ciS, ciL, ')')
