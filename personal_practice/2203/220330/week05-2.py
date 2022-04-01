A, B, C = map(int, input().split())
num = A * B * C
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while num != 0:
    digit = num % 10
    count[digit] += 1

    num //= 10

for i in range(10):
    print(f'{i}의 개수 는 {count[i]}개 입니다.')