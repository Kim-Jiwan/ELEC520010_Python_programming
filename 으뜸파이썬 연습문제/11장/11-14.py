import numpy as np

n = int(input())

a = np.zeros((n, n), dtype = "int32")

A = np.array([  [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 2, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]  ])

for i in range(0, a.shape[0]):
    a[i, i] = 1

a = np.flip(a, axis = 0)

for i in range(0, a.shape[0]):
    a[i, i] = 1

print(a)
