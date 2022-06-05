import numpy as np

A = [   [0, 1, 2],
        [3, 4, 5],
        [0, 2, 4],
        [6, 8, 10]  ]

A1 = [   [0, 1, 2],
        [3, 4, 5],
        [0, 2, 4],
        [6, 8, 10]  ]


B = np.concatenate((A[0:2], A[2:4]), axis = 1)

print(B)