'''def P(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return P(n - 2) + P(n - 3)'''

l = [1, 1, 1 ,2]

for n in range(4, 101):
    l.append(l[n - 2] + l[n - 3])


T = int(input())

for _ in range(T):
    num = int(input())
    print(l[num - 1])
