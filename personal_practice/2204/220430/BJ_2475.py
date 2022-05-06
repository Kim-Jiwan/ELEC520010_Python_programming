num_list = list(map(int, input().split()))
S = 0

for num in num_list:
    S += num ** 2

print(S % 10)