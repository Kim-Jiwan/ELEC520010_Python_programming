import numpy as np

a = np.array([0, 10, 20, 40, 60, 80])
b = np.array([0, 20])
c = np.array([], dtype = "int32")

for i in a:
    if i not in b:
        c = np.append(c, i)

c1 = np.setdiff1d(a, b)

print(c)
print(c1)