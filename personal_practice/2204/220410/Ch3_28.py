def is_palindrom(n):
    is_pal = False

    tmp = n
    n_reverse = 0 

    while tmp != 0:
        n_reverse = n_reverse * 10 + tmp % 10
        tmp //= 10

    if n_reverse == n:
        is_pal = True

    return is_pal

N = int(input("정수를 입력하시오 : "))

if is_palindrom(N):
    print(f"{N}은 거꾸로 정수입니다.")
else:
    print(f"{N}은 거꾸로 정수가 아닙니다.")