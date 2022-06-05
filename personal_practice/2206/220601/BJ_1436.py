N = int(input())

num = 666

while N > 0:
    if "666" in str(num):
        N -= 1
        num += 1
    else:
        num += 1

print(num - 1)