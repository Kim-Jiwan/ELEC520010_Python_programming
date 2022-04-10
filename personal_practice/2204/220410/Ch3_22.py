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

for i in range(2, 13):
    if is_prime_number(i):
        print(f"{i:2d} : 소수")
    else:
        print(f"{i:2d} : 합성수")