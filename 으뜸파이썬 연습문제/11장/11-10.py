import numpy as np

n = int(input())

a = np.ones((n, n), dtype = "int32")

for i in range(0, a.shape[0]):
    if i == 0 or i == a.shape[0] - 1:
        a[i, :] = 0
    else:
        a[i, 0], a[i, -1] = 0, 0

print(a)