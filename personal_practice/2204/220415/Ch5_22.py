n = int(input("n을 입력하시오 : "))

n_list = list(range(1, n * n + 1))

for i in range(1, n + 1):

    if i % 2 == 1:
        for j in range(n):
            print(f"{n_list[n * (i - 1) + j]:2d}", end = ' ')
            # :.2는 소수점을 나타냄! 그래서 f랑 같이 쓰인다
    else:
        for j in range(n):
            print(f"{n_list[n * (i - 1) + n - 1 - j]:2d}", end = ' ')

    print()

for i in range(1, n + 1):

    if i % 2 == 1:
        print(n_list[n * (i - 1) : n * (i - 1) + n])
            # :.2는 소수점을 나타냄! 그래서 f랑 같이 쓰인다
    else:
        print(n_list[n * (i - 1) + (n - 1) : n * (i - 1)])

    print()