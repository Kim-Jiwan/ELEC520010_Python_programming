# 2017110292 김지완
import numpy as np

y = np.array([  [80, 120, 40],
                [60, 80, 120],
                [40, 40, 40]    ])

y_concat = np.concatenate((y[0], y[1], y[2]), axis = 0)
num_set_y = sorted(list(set(y_concat)), reverse = False)

print(y)

for num in num_set_y:
    print(f"{num:3d} : {list(y_concat).count(num)}번")