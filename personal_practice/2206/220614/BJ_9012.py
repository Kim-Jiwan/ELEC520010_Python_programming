N = int(input())

for _ in range(N):
    ps = input()
    stack = []

    for p in ps:
        if p == "(":
            stack.append(p)
        elif p == ")":
            stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")
        