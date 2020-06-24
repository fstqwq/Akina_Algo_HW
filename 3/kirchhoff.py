import numpy as np
n, m = map(int, input().split())
K = np.zeros((n, n), dtype=np.int64)
for i in range(m):
    u, v = map(lambda x:int(x) - 1, input().split())
    K[u][u] -= 1
    K[v][v] -= 1
    K[u][v] += 1
    K[v][u] += 1
K = np.delete(K, 0, 0)
K = np.delete(K, 0, 1)
print(int(round(np.linalg.det(K))))