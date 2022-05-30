year, month, day = map(int, input("연월일을 .으로 구분하여 입력하시오 : ").split("."))

if year > 2000:
    print("20세기가 아닙니다.")
    print("제대로 된 입력이 아닙니다.")

