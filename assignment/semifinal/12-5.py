def get_nth(array, n):
    
    if n % (array.shape[1] * array.shape[2]) == 0:
        index_axis_0 = n // (array.shape[1] * array.shape[2]) - 1
        index_axis_1 = array.shape[1] - 1
        index_axis_2 = array.shape[2] - 1
        
    else:
        index_axis_0 = n // (array.shape[1] * array.shape[2])
        n %= (array.shape[1] * array.shape[2])
    
        if n % array.shape[2] == 0:
            index_axis_1 = n // array.shape[2] - 1
            index_axis_2 = 1
        else:
            index_axis_1 = n // array.shape[2]
            index_axis_2 = n % array.shape[2] - 1

    # print(index_axis_0, index_axis_1, index_axis_2)

    return array[index_axis_0, index_axis_1, index_axis_2]

import numpy as np

a = np.arange(0, 24).reshape(4, 3, 2)
b = np.arange(0, 60).reshape(5, 4, 3)


# for i in range(1, 25):
#     print(f"{i} th : {get_nth(a, i)}")

for i in range(3, 61, 3):
    print(f"{i} th : {get_nth(b, i)}")