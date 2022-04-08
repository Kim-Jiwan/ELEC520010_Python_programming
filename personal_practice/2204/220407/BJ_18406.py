N = int(input())
tmp = N
num_digit = 0
sum_left, sum_right = 0, 0

# 1. 자릿수 check
while tmp != 0:
    tmp //= 10
    num_digit += 1

# 2. 양쪽 수의 자릿수 더하기
for i in range(int(num_digit / 2)):
    sum_right += N % 10
    N //= 10

for i in range(int(num_digit / 2)):
    sum_left += N % 10
    N //= 10

if sum_right == sum_left:
    print("LUCKY")
else:
    print("READY")

