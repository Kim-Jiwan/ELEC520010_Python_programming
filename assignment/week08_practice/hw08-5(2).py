# 2017110292 김지완
rd_num_list = open("randint30.txt", "r")
raw_rd_num_list = rd_num_list.readline()

num_list = list(map(int, raw_rd_num_list.split()))

for num in range(1, 11):
    print(f"{num:2d} : {num_list.count(num)} 개")