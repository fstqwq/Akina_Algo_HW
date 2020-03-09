from cs_217 import *
import numpy as np
import math
from matplotlib import pyplot as plt
import pandas as pd

# Recursive Algorithm for the Binomial Coefficien
def Rec(n, k):
    if k < 0 or k > n:
        return 0
    if n == 0:
        return 1
    return Rec(n - 1, k - 1) + Rec(n - 1, k)

# Dynamic Programming Algorithm for the Binomial Coefficient
def DP(n,k):
    if k < 0 or k > n: return 0
    f=[[0 for i in range(k+1)] for j in range(n+1)]
    f[0][0] = 1
    for i in range(1, n+1):
        f[i][0] = 1
        for j in range(1, k+1):
            f[i][j]=f[i-1][j]+f[i-1][j-1]
    return f[n][k]

def C(n, m):
    ret = 1
    for i in range(m):
        ret = ret * (n - i)
        ret = ret // (i + 1)
    return ret

def calc(n, k):
    ret = 0.
    n = int(n.astype(np.uint8))
    k = int(k.astype(np.uint8))
    print("calc = ", n, k)
    for i in range(n + 1):
        for j in range(i + 1):
            a = C(n - i, k - j)
            b = C(i, j)
            ret += a * math.log(b)
    print("ret = ", ret)
    return ret
'''
print(DP(10, 0), C(10, 0))
print(DP(10, 5), C(10, 5))
print(DP(10, 10), C(10, 10))

x = [7., 8., 9., 10., 11., 12., 13.]
y = [4.47240000e-03, 1.01028000e-02, 3.42573000e-02, 1.51667000e-01, 6.74162100e-01, 3.11844440e+00, 1.94903846e+01]
z = [3.63408749e+05, 2.90726999e+06, 2.32581599e+07, 1.86065279e+08, 1.48852224e+09, 1.19081779e+10, 9.52654231e+10]
'''
x = []
y = []
z = []
for i in range(7, 14):
    x = np.append(x, i)
    n = 2 ** i
    k = n // 2
    print(n, k)
    y = np.append(y, measure_alg(DP, n, k))
    z = np.append(z, k * k * n * math.log(2))
    print(x)
    print(y)
    print(z)
exit()

for i in range(len(x)):
    x[i] = pow(2, x[i])
    y[i] *= 4e9
    y[i] = math.log(y[i])
    z[i] = math.log(z[i])
'''
Sum = np.concatenate((x, y, z))
Sum = pd.Series(Sum)
Sum.to_csv("DP.csv", index=None)
'''

plt.title("DP running time analysis(logarithm)")
plt.xlabel("x")
plt.ylabel("log(y)")
plt.plot(x, y, label = "Running Time (times 4e9)")
plt.plot(x, z, label = "The bound")
plt.legend()
plt.show()

