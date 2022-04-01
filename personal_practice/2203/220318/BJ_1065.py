num = int(input())

def han_num(NUM):
    cnt = 0

    for i in range(1, NUM + 1):

        if i < 100:
            cnt += 1
        else:
            digit_1 = i % 10
            digit_10 = i // 10 % 10
            digit_100 = i // 100

            if digit_1 - digit_10 == digit_10 - digit_100:
                cnt += 1

    return cnt

print(han_num(num))