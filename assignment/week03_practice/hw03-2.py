# 2017110292 김지완

x, y = map(int, input("점의 좌표를 x, y를 입력하시오 : ").split())

if (x * x + y * y) ** 0.5 == 5:
    print("원의 위에 있음")

elif (x * x + y * y) ** 0.5 > 5:
    print("원의 외부에 있음")

elif (x * x + y * y) ** 0.5 < 5:
    print("원의 내부에 있음")