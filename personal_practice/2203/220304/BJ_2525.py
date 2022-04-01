A, B = map(int, input().split())
C = int(input())

# 1번 풀이 -> 어렵게 풀었다..
if B + C >= 60:
    if (A + (B + C) // 60) >= 24:
        A = (A + (B + C) // 60) - 24
        B = (B + C) % 60
    else:
        A += (B + C) // 60
        B = (B + C) % 60
else:
    B += C

print(A, B)

# 2번 풀이 -> 쉽게 풀었다! 잼민이들 실습때 풀었던거
B += C
A += B // 60
B = B % 60

if A >= 24:
    A -= 24

# 두번만에 맞춤