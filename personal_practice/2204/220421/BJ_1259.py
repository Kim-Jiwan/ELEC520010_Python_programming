def is_parindrom(num):
    tmp = num
    num_parin = 0

    while tmp != 0:
        num_parin = num_parin * 10 + tmp % 10
        tmp //= 10

    return num == num_parin

while True:
    n = int(input())

    if n == 0:
        break
    else:
        print("yes") if is_parindrom(n) else print("no")