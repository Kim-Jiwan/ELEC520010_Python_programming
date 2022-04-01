T = int(input())

def fatorial(n):
    q = 1

    for i in range(1, n + 1):
        q *= i

    return q

for _ in range(T):
    N, M = map(int, input().split())
    ## N <= M

    print(fatorial(M) // ( fatorial(M - N) * fatorial(N) ))
    