import random as rd

f = open("random_numbers.txt", "w")

for _ in range(10):
    f.write(f"{rd.randint(1, 1000)} ")

f.close()


f = open("random_numbers.txt", "r")

nums = f.readline().rstrip()

even_num_list = [ int(num) for num in nums.split() if int(num) % 2 == 0 ]
odd_num_list = [ int(num) for num in nums.split() if int(num) % 2 == 1 ]


print(even_num_list)
print(odd_num_list)