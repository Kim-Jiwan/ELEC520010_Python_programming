# 2017110292 김지완
import numpy as np

a = np.random.random(10)

print(f"a = {a}")
print(f"최댓값 : {a.max()}")
print(f"최솟값 : {a.min()}")
print(f"평균값 : {a.sum() / len(a)}")