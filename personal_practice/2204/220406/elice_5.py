N = int(input())
M = int(input())
sum_odd = 0

for i in range(N, M + 1):
    if i % 2 == 1:
        sum_odd += i

print(sum_odd)