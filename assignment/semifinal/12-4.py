import numpy as np

n = int(input("n을 입력하시오 : "))
n_array = np.zeros((n, n), dtype = "int32")
# n_array = np.diag(1 + np.arange(n), k = 0)

n_array = np.diag(1 + np.zeros(n, dtype = "int32"), k = 0)
# for i in range(len(n_array)):
#     n_array[i, i] = 1

n_array = np.flip(n_array, axis = 0)



for i in range(len(n_array)):
    n_array[i, i] = 1

print(n_array)