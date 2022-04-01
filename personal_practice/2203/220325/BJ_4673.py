def d(n):
    s = n

    while n != 0:
        s += n % 10
        n //= 10

    return s

def is_self_num(n):
    self_num = True

    for i in range(n, 0, -1):
        if d(i) == n:
            self_num = False
            break

    return self_num

a = list(range(1, 10001))

for i in a:
    if is_self_num(i):
        print(i)