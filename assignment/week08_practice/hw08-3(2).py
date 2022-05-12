# 2017110292 김지완
rd_num_list = open("random_numbers.txt", "r")
rd_num_even = open("randon_even.txt", "w")

nums = rd_num_list.read()
num_list = nums.split()

for num in num_list:
    tmp = int(num)

    if tmp % 2 == 0:
        rd_num_even.write(f"{tmp} ")

    num = rd_num_list.read()

rd_num_list.close()
rd_num_even.close()