def is_prime_number(num):
    is_prime = True
    
    if num % 2 == 1:
        for i in range(3, num, 2):
            if num % i == 0:
                is_prime = False
                break
    else:
        is_prime = False
        
    return is_prime

while True:
    num = int(input("숫자를 입력하세요 : "))
    
    if num > 0:
        if is_prime_number(num):
            print(f"{num}은 소수입니다..")
        else:
            print(f"{num}은 소수가 아닙니다.")
    else:
        print("양수를 입력하세요.")
