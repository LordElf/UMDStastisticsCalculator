import numpy as np
from math import *
def info():
    choice = input("Setlect type of data set\n 1. normal 2.chi \n 3.normal approx to bino \n")
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
    elif(choice == "3"):
       run_bino()
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

def run_bino():
    p =input("probability on idividual test:\n")
    p = float(p)
    n = input("total num of trails :\n")
    n = int(n)
    x1 = input("num of success larger than:\n")
    x1 = int(x1)
    x2 = input("smaller than:\n")
    x2 = int(x2)
    phi_d = sqrt(n*p*(1-p))
    phi1 = (x1+0.5 - n*p) / phi_d
    phi2 = (x2 + .5 -n*p) / phi_d
    phi1 = input(f"find phi({phi1})\n")
    phi1 = float(phi1)
    phi2 = input(f"find phi({phi2})\n")
    phi2 = float(phi2)
    print(f"the prob is {phi2 - phi1}")

