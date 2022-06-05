import numpy as np

n = int(input())
A = np.zeros((n, n), dtype = "int32")

for i in range(0, A.shape[0]):
    A[i, 0 : i + 1] += 1

print(A)

print(np.sum(A))
print(np.sum(A, axis = 0))
print(np.sum(A, axis = 1))