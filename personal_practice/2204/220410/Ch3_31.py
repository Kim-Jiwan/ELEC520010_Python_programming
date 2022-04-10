def is_chinhwa(n):
    is_CH = False

    n_divisor = 0
    m = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            n_divisor += i

    for i in range(1, n_divisor // 2 + 1):
        if n_divisor % i == 0:
            m += i

    if n == m and n != n_divisor:
        is_CH = True

    return is_CH, n_divisor

for i in range(1, 20001):
    is_CH = is_chinhwa(i)

    if is_CH[0]:
        print(f"{i}의 친화수 {is_CH[1]}")