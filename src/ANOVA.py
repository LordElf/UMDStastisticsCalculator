import numpy as np
from math import *

data = []
data.append('5.3	4.6	5.9	6.2	6.6	5.7')
data.append('6.6	8.1	6.2	7.4	5.8	5.5')
data.append('5.9	4.8	6.4	4.9	5.9	5.1')
data.append('8.2	6.1	7.8	7.1	5.5	7.2')

for i in range(0, len(data)):
    data[i] = data[i].replace(',', ' ')
    data[i] = data[i].split()
    data[i] = np.array(data[i]).astype(np.float)

# Source of variation   |   df      |   Sum of Squares  |   Mean Square     |   f
# Treatment             |   I-1     |   SSTr            |   MSTr            |   MSTr/MSE
#   Error               |   I(j-1)  |   SSE             |   MSE
#   Total               |   IJ-1    |   SST
I = len(data)
J = len(data[0])
print(I, J)
Sum = np.sum(data, axis=1) 
u = np.mean(data, axis=1)
xdda = np.mean(data)
SST = np.sum((data - xdda)**2)
SSTr = np.sum((u - xdda)**2) * J
SSE = 0
for i in range(0,len(data)):
    SSE += np.sum((data[i] - u[i])**2)
MSTr = SSTr / (I - 1)
MSE = SSE / (I * (J - 1))
F = MSTr/MSE
SSE = round(SSE, 4)
SST = round(SST, 4)
SSTr = round(SSTr, 4)
MSTr = round(MSTr, 4)
MSE = round(MSE, 4)
F = round(F, 4)
print(data)
print(u)
print(f"Source of variation   |   df      |   Sum of Squares  |   Mean Square     |   f \nTreatment             |   {I-1}       |   {SSTr}          |   {MSTr}          |   {F}\n  Error               |   {I * (J-1)}      |   {SSE}          |   {MSE}\n  Total               |   {I*J-1}      |   {SST}")
Q = 3.77
w = round(Q * sqrt(MSE / J), 4)
print("w ", w)
