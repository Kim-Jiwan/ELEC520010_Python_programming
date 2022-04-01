n = int(input())
a = []

for _ in range(n):
    tmp = int(input())
    a.append(tmp)

for i in range(n):
    print(f"{a[i]:2d}", end = ' ')
    print("*" * a[i])