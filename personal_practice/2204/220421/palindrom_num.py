def palindrom(num):
    num_pal = 0

    while num != 0:
        num_pal = num_pal * 10 + num % 10
        num //= 10

    return num_pal

num = int(input("숫자를 입력하세요 : "))

if num == palindrom(num):
    print(f"{num}   {palindrom(num)}")
    print(f"{num}은 팔린드롬입니다.")
else:
    print(f"{num}   {palindrom(num)}")
    print(f"{num}은 팔린드롬이 아닙니다.")