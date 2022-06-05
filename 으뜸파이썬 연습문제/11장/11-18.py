import numpy as np

A = np.array([[1, 1, -1], [3, 2 ,3], [6, 7, 8]])
B = np.array([[1, 4, -6], [0, 1, 1], [3, -1 ,6]])

print(f"(1)\n {2 * A}")
print(f"(2)\n {A + B}")
print(f"(3)\n {A - B}")
print(f"(4)\n {np.matmul(A, B)}")
print(f"(5)\n {3 * A - 2 * B}")
print(f"(6)\n {np.linalg.det(A)}")
print(f"(7)\n {np.linalg.det(B)}")
print(f"(8)\n {np.sum(A, axis = 0)}")
print(f"(9)\n {np.sum(B, axis = 0)}")
print(f"(10)\n {np.sum(A, axis = 1)}")
print(f"(11)\n {np.sum(B, axis = 1)}")