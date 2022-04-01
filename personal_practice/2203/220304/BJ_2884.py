H, M = map(int, input().split())


if M < 45:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = M + 15
else:
    M -= 45

print(H, M)

# 3번만에 맞춤