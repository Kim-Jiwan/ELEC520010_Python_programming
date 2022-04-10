def is_prime_number(num):
    is_prime_num = True

    if num == 2:
        True

    elif num % 2 == 0:
        is_prime_num = False
    
    else:
        for i in range(3, num, 2):
            if num % i == 0:
                is_prime_num = False
                break

    return is_prime_num

while True:
    N = int(input("숫자를 입력하세요 : "))

    if N > 0:
        if is_prime_number(N):
            print(f"{N}은 소수입니다.")
        else:
            print(f"{N}은 소수가 아닙니다.")
    else:
        print("프로그램을 종료합니다.")
        break