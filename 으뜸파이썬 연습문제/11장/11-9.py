import numpy as np

n = int(input())

a = np.ones((n, n), dtype = "int32")

for i in range(1, a.shape[0] - 1):
    a[1 : -1, 1 : -1] = 0

print(a)