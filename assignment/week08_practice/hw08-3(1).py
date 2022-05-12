# 2017110292 김지완
import random as rd

num_list = [ rd.randint(1, 1000) for _ in range(10) ]

f = open("random_numbers.txt", "w")

for num in num_list:
    f.write(f"{str(num)} ")

f.close()