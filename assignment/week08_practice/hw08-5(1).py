# 2017110292 김지완
import random as rd

num_list = [ rd.randint(1, 10) for _ in range(30) ]

rd_num_list = open("randint30.txt", "w")

for num in num_list:
    rd_num_list.write(f"{num} ")