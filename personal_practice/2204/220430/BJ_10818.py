N = int(input())
num_list = list(map(int, input().split()))

print(min(num_list), max(num_list))

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)

    except EOFError:
        break