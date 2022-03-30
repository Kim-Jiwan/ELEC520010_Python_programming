n = int(input())
A = list(map(int, input().split()))

cnt_odd, cnt_even = 0, 0

for i in range(n):
    if A[i] % 2 == 1:
        cnt_odd += 1
    else:
        cnt_even += 1

print(f"{cnt_odd}\n{cnt_even}")