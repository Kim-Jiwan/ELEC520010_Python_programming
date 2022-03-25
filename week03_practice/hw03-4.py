# 2017110292 김지완

up_per_day, down_per_day, target = 7, 5, 30
cnt = 0
height = 0

while True:
    cnt += 1

    height += up_per_day

    print("day : {:2d}  달팽이의 위치 : {:2d} 미터".format(cnt, height))

    if height >= target:
        break

    height -= down_per_day