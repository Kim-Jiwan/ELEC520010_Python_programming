def isPrime(num):
    is_prime = True

    if num < 2:
        is_prime = False
    elif num == 2:
        is_prime = True
    elif num % 2 == 0:
        is_prime = False
    else:
        for i in range(3, (num // 3) + 1, 2):
            if num % i == 0:
                is_prime = False
                break

    return is_prime

num = int(input("숫자를 입력하세요 : "))
list_prime = []

if isPrime(num):
    print(f"{num}은 소수입니다.")
elif ~(isPrime(num)):
    print(f"{num}은 소수가 아닙니다.")

for i in range(2, 10001):
    if isPrime(i):
        list_prime.append(i)

print(list_prime)