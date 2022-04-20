A, B, V = map(int, input().split())
cnt = 0

cnt += (V - B) // (A - B)

cnt += 1 if (V - B) % (A - B) != 0 else 0

print(cnt)