N = int(input())

print("*" * N + " " * (2 * N - 3) + "*" * N)

for i in range((2 * N - 3) // 2):
    print(" " * (i + 1) + "*" + " " * (N - 2) + "*" + " " * (2 * (N - i) - 5) + "*" + " " * (N - 2) + "*")

print(" " * (N - 1) + "*" + " " * (N - 2) + "*" + " " * (N - 2) + "*")

for i in range((2 * N - 3) // 2 - 1, -1, -1):
    print(" " * (i + 1) + "*" + " " * (N - 2) + "*" + " " * (2 * (N - i) - 5) + "*" + " " * (N - 2) + "*")

print("*" * N + " " * (2 * N - 3) + "*" * N)