N = input()
N = sorted(N, reverse = True)
N_int = [ int(n) for n in N ]

if '0' not in N:
    print(-1)
else:
    if sum(N_int) % 3 != 0:
        print(-1)
    else:
        print("".join(N))
        for n in N:
            print(n, end = '')