# 시간초과난다..!!
# 3개씩 끊을 방법을 찾아보자
# 문자열 list로 처리하기?

Bin_num = input()

def B_to_O(Bin):
    oct = 0
    digit_oct = 0

    while Bin != 0:
        digit_bin = 0
        tmp_oct = 0

        for i in range(3):
            tmp = Bin % 10
            Bin //= 10

            tmp_oct += tmp * (2 ** digit_bin)
            digit_bin += 1
        
        oct += tmp_oct * (10 ** digit_oct)

        digit_oct += 1

    return oct

Bin_num = int(input())

print(B_to_O(Bin_num))