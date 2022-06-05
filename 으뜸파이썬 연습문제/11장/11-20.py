import numpy as np

a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([16, 9, 3])

solution = np.linalg.solve(a, b)

print(f"x = {solution[0]:.1f}, y = {solution[1]:.1f}, z = {solution[2]:.1f}")

print(np.linalg.det(a))