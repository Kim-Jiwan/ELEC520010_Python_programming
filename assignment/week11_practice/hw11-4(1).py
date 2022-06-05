# 2017110292 김지완
import numpy as np

x = np.array([  [10, 20, 40, 60],
                [10, 20, 40, 40]    ])

x_concat = np.concatenate((x[0], x[1]), axis = 0)
num_set_x = sorted(list(set(x_concat)), reverse = False)

print(x)

for num in num_set_x:
    print(f"{num:3d} : {list(x_concat).count(num)}번")