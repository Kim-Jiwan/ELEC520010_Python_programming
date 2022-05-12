import time

def mac_operation(Z, X, Y):

    return Z + X * Y

def matrix_mul(X, Y):
    result = [  [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]   ]

    for i in range(len(result)):
        for j in range(len(result)):
            for k in range(len(result)):
                result[i][j] = mac_operation(result[i][j], X[i][k], Y[k][j])
                # result[i][j] += X[i][k] * Y[k][j]
                # result[i][j] = result[i][j] + X[i][k] * Y[k][j]
    
    return result

A = [   [1, 2, 3, 1],
        [4, 5, 6, 1],
        [7, 8, 9, 1],
        [1, 3, 2, 1]   ]

B = [   [9, 8, 7, 1],
        [6, 5, 4, 1],
        [3, 2, 1, 1],
        [1, 2, 3, 1]   ]

print(A[:-1])

"""start_time = time.time()

Z = matrix_mul(A, B)

end_time = time.time()

print(f"{Z[0]}\n{Z[1]}\n{Z[2]}")

print(f"{end_time - start_time == 0.0}")"""