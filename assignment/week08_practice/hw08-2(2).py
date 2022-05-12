# 2017110292 김지완
list1 = open("number1to10.txt", "r")
list2 = open("numberby10.txt", "r")
list_merge = open("merge.txt", "w")

line_num = list1.readline().rstrip()
num = list2.readline().rstrip()

while line_num and num:
    list_merge.write(f"{line_num} : {num}\n")

    line_num = list1.readline().rstrip()
    num = list2.readline().rstrip()

list1.close()
list2.close()
list_merge.close()    