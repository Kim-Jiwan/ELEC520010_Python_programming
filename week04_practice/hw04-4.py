# 2017110292 김지완

Pi = 3.141592

def area_and_circumference(r):
    print("넓이 : {:7.3f}, 둘레 : {:7.3f}".format(Pi * r ** 2, 2 * Pi * r))

while True:
    r = int(input("반지름을 입력하시오 : "))

    if r < 0:
        print("프로그램을 종료합니다.")
        break
    else:
        area_and_circumference(r)