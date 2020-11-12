import numpy as np
from math import *

data = []
data.append('10 15 8 12 15')
data.append('14 18 21 15')
data.append('17 16 14 15 17 15 18')

for i in range(0, len(data)):
    data[i] = data[i].replace(',', ' ')
    data[i] = data[i].split()
    data[i] = np.array(data[i]).astype(np.float)

I = len(data)
J = len(data[0])
n = 0
for i in range(0, len(data)):
    n += len(data[i])

# Source of variation   |   df      |   Sum of Squares  |   Mean Square     |   f
# Treatment             |   I-1     |   SSTr            |   MSTr            |   MSTr/MSE
#   Error               |   I(j-1)  |   SSE             |   MSE
#   Total               |   IJ-1    |   SST
print(I, J)
u = []
for i in range(0, len(data)):
    u.append(sum(data[i])/len(data[i]))
print(u)
xdda = sum(u)/len(u) 
print(xdda)
#SST = np.sum((data - xdda)**2)
SST = 0
for i in range(0, I):
    SST += sum((data[i] - xdda)**2)
#SSTr = np.sum((u - xdda)**2) * J
SSTr = 0
for i in range(0, I):
    for j in range(0, len(data[i])):
        SSTr += (u[i] - xdda)**2 
SSE = 0
# or sum(s**2)/I
for i in range(0,len(data)):
    SSE += sum((data[i] - u[i])**2)
MSTr = SSTr / (I - 1)
# n = Signma{Ji}
MSE = SSE / (n-I)
F = MSTr/MSE
SSE = round(SSE, 4)
SST = round(SST, 4)
SSTr = round(SSTr, 4)
MSTr = round(MSTr, 4)
MSE = round(MSE, 4)
F = round(F, 4)
print(data)
print(f"Source of variation   |   df      |   Sum of Squares  |   Mean Square     |   f \nTreatment             |   {I-1}       |   {SSTr}          |   {MSTr}          |   {F}\n  Error               |   {n}      |   {SSE}          |   {MSE}\n  Total               |   {n-1}      |   {SST}")
Q = 3.65 
w = round(Q * sqrt(MSE / J), 4)
print("w ", w)
print(u)
