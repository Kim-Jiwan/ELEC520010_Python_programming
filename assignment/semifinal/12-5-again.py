import numpy as np

def get_nth(a, n):

    if n % (a.shape[1] * a.shape[2]) == 0:
        index_axis_0 = n // (a.shape[1] * a.shape[2]) - 1
        index_axis_1 = -1
        index_axis_2 = -1

    else:
        index_axis_0 = n // (a.shape[1] * a.shape[2])
        n %= (a.shape[1] * a.shape[2])

        if n % a.shape[2] == 0:
            index_axis_1 = n // a.shape[2] - 1
            index_axis_2 = -1
        
        else:
            index_axis_1 = n // a.shape[2]
            index_axis_2 = n % a.shape[2] - 1

    # print(index_axis_0, index_axis_1, index_axis_2)
    return a[index_axis_0, index_axis_1, index_axis_2]

# n = int(input())
a = np.arange(0, 24).reshape(4, 3, 2)
b = np.arange(0, 60).reshape(5, 4, 3)

for i in range(1, 61):
    print(f"{i} th element is {get_nth(b, i)}")