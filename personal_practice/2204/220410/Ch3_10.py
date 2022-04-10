a, b = map(int, input("두 정수를 입력하시오 : ").split())

if a % b == 0:
    print(f"{a}는(은) {b}의 배수입니다.")
else:
    print(f"{a}는(은) {b}의 배수가 아닙니다.")