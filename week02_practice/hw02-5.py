# 2017110292 김지완

N = int(input("정수를 입력하세요 : "))
D = int(input("자리수를 입력하세요 : "))

print("백의 자리:", N // 100)
print("십의 자리:", N //10 % 10)
print("일의 자리:", N % 10)

def what_digit(digit, num):
    for i in range(1, digit):
        num //= 10
    print(num % 10)

what_digit(D, N)