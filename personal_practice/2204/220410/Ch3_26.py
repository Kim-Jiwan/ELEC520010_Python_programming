"""n = int(input("n을 입력하시오 : "))
cnt = list(range(1, n + 1))

for i in range(n):
    for j in range(n):
        print(f"{cnt[j]:3d}", end = "")

    for j in range(n):
        cnt[j] += n

    cnt.reverse()    

    print()"""

N = int(input("n을 입력하시오 : "))
snake = 0

for i in range(1, N+ 1):
    if i == 1:
        for j in range(N):
            snake += 1
            print(f"{snake:4d}", end = "")

    elif i % 2 == 1:
        snake += N - 1
        for j in range(1, N+ 1):
            snake += 1
            print(f"{snake:4d}", end = "")

    elif i % 2 == 0:
        snake += N + 1
        for j in range(1, N+ 1):
            snake -= 1
            print(f"{snake:4d}", end = "")

    print()