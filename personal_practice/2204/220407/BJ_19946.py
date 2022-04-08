N = int(input())

# 1. 실수한 부분 찾기 -> 홀수가 나오면 계산 실수한 것이다.
while N % 2 == 0:
    N = N // 2

# 2. 실수한 부분이 2의 몇 제곱인지 찾기
num_mis = N + 1
cnt_mis = 0

while num_mis != 1:
    num_mis = num_mis // 2
    cnt_mis += 1

print(cnt_mis)