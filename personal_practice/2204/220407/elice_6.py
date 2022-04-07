N = int(input())
square_cnt = 0

for _ in range(N):
    num = int(input())
    i = 1

    while i ** 2 < num:
        i += 1
        
    if i ** 2 == num:
        square_cnt += 1

print(square_cnt)