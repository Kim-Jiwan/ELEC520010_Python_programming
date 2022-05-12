N, K = map(int, input().split())

N -= int(K * (K + 1) / 2)
K_list = [ i for i in range(1, K + 1) ]

# 가장 많이 담긴 - 가장 적게 담긴 이 가장 적도록
# 나눠 담을 수 없는 경우(모두 다르게)

if N < 0:
    print(-1)
elif N == 0:
    print(K_list[-1] - K_list[0])
elif N > 0:
    print(K_list[-1])
