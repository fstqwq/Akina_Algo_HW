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
    f=[[1 for i in range(0,k+1)] for j in range(0,n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if (i <= j):
                f[i][j] = 1
            else:
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

ret = [[8, 0.017284399999999978], [9, 0.06506279999999998], [10, 0.2480131], [11, 0.8866936], [12, 3.1019144], [13, 13.012815399999997], [14, 44.0824429]]

x = np.array([])
y = np.array([])
z = np.array([])
w = np.array([])
for i in range(len(ret)):
    x = np.append(x, ret[i][0])
    y = np.append(y, ret[i][1] * 5.5e7)
    z = np.append(z, pow(1.855, 2 * x[i]) * x[i] * math.log(2) * 8)
    w = np.append(w, calc(2 * x[i], x[i]) * 45) 


for i in range(len(x)):
    y[i] = y[i]
    z[i] = z[i]
    w[i] = w[i]
'''
Sum = np.concatenate((x, y, z, w))
Sum = pd.Series(Sum)
Sum.to_csv("rec.csv", index=None)
'''
plt.title("Recursion running time analysis(logarithm)")
plt.xlabel("x")
plt.ylabel("log(y)")
plt.plot(x, y, label = "Running Time (times 5.5e7)")
plt.plot(x, z, label = "The bound")
plt.plot(x, w, label = "Precise bit operation (times 44)")
plt.legend()
plt.show()

