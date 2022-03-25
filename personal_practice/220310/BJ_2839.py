N = int(input())
cnt = 0

# 최대한 적은 봉지를 가져간다!

cnt += (N // 5)
N = (N % 5)

cnt += (N // 3)
N = (N % 3)

if N == 0:
    print(cnt)
else:
    print(-1)