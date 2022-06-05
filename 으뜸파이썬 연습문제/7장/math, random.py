import math as m
import random as rd

print(m.sin(m.radians(90)))

print(rd.random())

rand_list = [ rd.randint(1, 10) for _ in range(10) ]

print(rand_list)

rd.shuffle(rand_list)
print(rand_list)

for i in range(1, 11):
    print(f"sqrt({i:2d}) = {m.sqrt(i):.3f}")