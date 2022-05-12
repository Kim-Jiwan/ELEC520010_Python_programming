# 2017110292 김지완
rd_num_list = open("random_numbers.txt", "r")
rd_num_odd = open("randon_odd.txt", "w")

nums = rd_num_list.read()
num_list = nums.split()

for num in num_list:
    tmp = int(num)

    if tmp % 2 == 1:
        rd_num_odd.write(f"{tmp} ")

    num = rd_num_list.read()

rd_num_list.close()
rd_num_odd.close()