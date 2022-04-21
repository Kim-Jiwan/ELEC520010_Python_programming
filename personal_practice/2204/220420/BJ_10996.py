N = int(input())

for i in range(N * 2):
    if i % 2 == 0:
        # j가 홀수면 별
        # j가 짝수면 공백
        for j in range(N):
            if j % 2 == 0:
                print("*", end = "")
            else:
                print(" ", end = "")
    else:
        # j가 홀수면 공백
        # j가 짝수면 별
        for j in range(N):
            if j % 2 == 0:
                print(" ", end = "")
            else:
                print("*", end = "")
    print()