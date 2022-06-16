# 2017110292 김지완
import random as rd

num = rd.randint(1, 20)
print(num)
cnt = 0

while True:
    user_num = int(input("1 ~ 20까지의 숫자를 입력하세요 : "))

    if num < user_num:
        print(f"{user_num}보다 작습니다.")
        cnt += 1
    elif num > user_num:
        print(f"{user_num}보다 큽니다.")
        cnt += 1
    elif num == user_num:
        print("정답입니다!")
        cnt += 1
        break

if cnt <= 3:
    print(f"{cnt}번 만에 맞춘 당신은 A+")
elif cnt > 3 and cnt <= 6:
    print(f"{cnt}번 만에 맞추셨네요. B+")
elif cnt >= 7:
    print(f"{cnt}번 만에 맞추다니... 재수강각ㅋㅋ")