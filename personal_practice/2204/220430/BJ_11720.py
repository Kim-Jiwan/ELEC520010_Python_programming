N = int(input())
num = int(input())
S = 0

for i in range(N):
    S += num % 10
    num //= 10

print(S)