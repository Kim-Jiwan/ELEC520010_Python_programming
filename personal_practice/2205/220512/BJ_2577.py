A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num_cnt = [ 0 for _ in range(10)]

while num != 0:
    tmp = num % 10
    num_cnt[tmp] += 1
    num //= 10

for num in num_cnt:
    print(num)