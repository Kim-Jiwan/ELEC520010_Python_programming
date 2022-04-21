# 2017110292 김지완

print("1)덧셈   2)뺼셈   3)곱셈   4)나눗셈")
operation_num = int(input("어떤 연산을 원하는지 번호를 입력하세요 :"))

if operation_num == 1 or operation_num == 2 or operation_num == 3 or operation_num == 4:

    print("연산을 원하는 숫자 두개를 입력하세요")

    X = int(input())
    Y = int(input())

    if operation_num == 1:
        print(f"{X} + {Y} = {X + Y}")

    elif operation_num == 2:
        print(f"{X} - {Y} = {X - Y}")

    elif operation_num == 3:
        print(f"{X} * {Y} = {X * Y}")

    elif operation_num == 4:
        print(f"{X} / {Y} = {X / Y}")

else:
    print("잘못 입력하셨습니다.")