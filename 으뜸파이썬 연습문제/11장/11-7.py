import numpy as np

n = int(input())

a = np.zeros((n, n), dtype = "int32")

for i in range(0, a.shape[0]):
    if i % 2 == 0:
        a[i, 0::2] = 1
    else:
        a[i, 1::2] = 1

print(a)