N = int(input())
coin_num = 0

if N == 1 or N == 3: # 거슬러 줄 수 없는 경우 -> exception
    coin_num = -1

elif N % 5 != 0:
    coin_num += N // 5
    N %= 5
    
    if N % 2 == 0:
        coin_num += N // 2
    else:
        N += 5
        coin_num -= 1 # 5원 discount
        coin_num += N // 2

elif N % 5 == 0:
    coin_num += N // 5

print(coin_num)