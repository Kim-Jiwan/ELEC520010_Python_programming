init_fuel = 500
current_fuel = init_fuel

while True:
    use_fuel = int(input("충전 또느 사용한 연료를 +/- 기호와 함께 임력하시오 : "))

    current_fuel += use_fuel

    if current_fuel >= init_fuel / 10:
        print(f"현재 탱크양은 {current_fuel}입니다.")
    else:
        print(f"현재 탱크양은 {current_fuel}입니다.")
        print("경고 : 연로가 10% 미만이니 충전하세요!")
        break