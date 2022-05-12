# 2017110292 김지완
f = open("number1to10.txt", "w")

for num in range(1, 11):
    f.write(f"{str(num)}\n")

f.close()

f_num = open("number1to10.txt", "r")
f_num_by_10 = open("numberby10.txt", "w")

num = f_num.readline()

while num:
    f_num_by_10.write(f"{int(num) * 10}\n")

    num = f_num.readline()

f_num.close()
f_num_by_10.close()