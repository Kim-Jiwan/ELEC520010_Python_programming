from tkinter import E


def resident_num(num):
    day = num % 100
    num //= 100
    month = num % 100
    num //= 100
    year = num
    
    if year >= 50:
        print(f"19{year}년 {month}월 {day}일")
    elif year < 50:
        if year < 10:
            print(f"200{year}년 {month}월 {day}일")
        else:
            print(f"20{year}년 {month}월 {day}일")

while True:
    num = int(input("주민등록번호 첫 6숫자 형식 입력 : "))

    if type(num) != int:
        print("숫자를 입력하세요")
    elif num == -1:
        print("종료합니다.")
        break
    else:
        resident_num(num)