# 2017110292 김지완

# n이 홀수 이면서, range(3, n, 2)인 m에 대해 n % m을 담은 list에 0이 없는 경우 
# 즉, 홀수이면서 n보다 작은 홀수 m에 대해 나누어 떨어지지 않는 n을 prime_list에 추가하는 알고리즘
prime_list = [ n for n in range(10, 51) if (n % 2 == 1) and (0 not in [ n % m for m in range(3, n, 2) ]) ]

print(prime_list)