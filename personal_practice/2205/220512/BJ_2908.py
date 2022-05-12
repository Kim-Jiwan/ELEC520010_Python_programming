def num_reverse(num):
    result = 0

    while num != 0:
        tmp = num % 10
        result = result * 10 + tmp
        num //= 10

    return result

A, B = map(int, input().split())

A_reverse, B_reverse = num_reverse(A), num_reverse(B)

print(max([A_reverse, B_reverse]))