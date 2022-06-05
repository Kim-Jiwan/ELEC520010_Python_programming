# 2017110292 김지완
import numpy as np

n = int(input("n을 입력하시오 : "))

a = np.full((n, n), 0)
# a = np.diag(1 + np.arange(n), k = 0)

for i in range(n):
    a[i, i] += i + 1

print(a)