K = int(input())

A = [0, 0, 1, 1]
B = [0, 1, 1, 2]

for i in range(3, 45):
    A.append(A[i] + A[i-1])
    B.append(B[i] + B[i-1])

print(A[K], B[K])