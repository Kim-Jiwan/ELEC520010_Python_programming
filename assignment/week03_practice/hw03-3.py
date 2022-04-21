# 2017110292 김지완

num = int(input("숫자를 입력하세요 : "))

for i in range(1, num + 1):
    for _ in range(1, num - i + 1):
        print(" ", end = '')
    for _ in range(1, i + 1):
        print("*", end ='')
    print()