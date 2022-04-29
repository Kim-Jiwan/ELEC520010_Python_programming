import sys


T = int(input())
# 초 단위로 입력받음

A_cnt, B_cnt, C_cnt = 0, 0, 0
# A : 5분, B : 1분, C : 10초


if T % 300 == 0:
    A_cnt += T // 300
    
else:
    while T >= 0:
        T -= 60
        B_cnt += 1

        if T % 300 == 0:
            A_cnt += T // 300
            break
    else:
        print(-1)