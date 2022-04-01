N = int(input())
bong_count = 0

if N % 5 == 0:
    bong_count += N // 5
    # 5kg로 담는 것이 우선순위가 가장 높다.
    # -> // 연산자로 한꺼번에 담는다.
else:
    while N >= 0:
        N -= 3
        bong_count += 1
        # 3kg은 우선순위가 낮으므로 한 개씩 추가하며 우선순위가 더 높은 5kg가 들어갈 수 있는 가능성을 검토한다.
        
        if N % 5 == 0:
            bong_count += N // 5
            break

    else:
        bong_count = -1 
        # 4, 7 이런 경우는 3과 5로 조합할 수 없으므로 3씩 계속 빼다보면 음수가 되어 while문을 탈출한다.

print(bong_count)