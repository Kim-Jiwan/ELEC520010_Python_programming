# 2017110292 김지완
import numpy as np

n = int(input("n을 입력하시오 : "))

a = np.zeros((n, n), dtype = "int32")

for i in range(n):
    a[i, 0:i + 1] += 1

print(a)