def is_armstrong(num):
    # 함수의 인자가 함수 내에서 바뀐다면 다른 변수 tmp에 저장해두자
    is_armst = False
    tmp = num

    digit_1 = num % 10
    num //= 10
    digit_10 = num % 10
    num //= 10
    digit_100 = num % 10

    if ((digit_1 ** 3) + (digit_10 ** 3) + (digit_100 ** 3)) == tmp:
        is_armst = True 

    return is_armst

armst_list = []

for i in range(100, 1000):
    if is_armstrong(i):
        armst_list.append(i)

print("세 자리의 암스트롱 수 : ", end = '')

for val in armst_list:
    print(val, end = ' ')