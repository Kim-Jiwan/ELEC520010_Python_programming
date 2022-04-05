start = input()
P, duck = "문제", "고무오리"
P_cnt = 0

if start == "고무오리 디버깅 시작":
    while str != "고무오리 디버깅 끝":
        str = input()

        if str == P:
            P_cnt += 1
        elif str == duck:
            if P_cnt > 0:
                P_cnt -= 1
            elif P_cnt == 0:
                P_cnt += 2

if P_cnt == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")