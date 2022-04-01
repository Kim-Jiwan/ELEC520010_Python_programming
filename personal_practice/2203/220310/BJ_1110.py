N = int(input())
cnt = 0
A, B  = 0, 0
N_cycle = N

# 26 -> 2 + 6 = 8 ->

A = N_cycle // 10
B = N_cycle % 10
# N = B * 10 + (A + B)
N_cycle = B * 10 + (A + B) % 10
cnt += 1

while N != N_cycle:

    A = N_cycle // 10
    B = N_cycle % 10
    # N = B * 10 + (A + B)
    N_cycle = B * 10 + (A + B) % 10
    cnt += 1

print(cnt)