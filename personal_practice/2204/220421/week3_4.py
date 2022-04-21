depth = 30
A, B = 7, 5
day = 0
current_position = 0

while True:
    day += 1
    current_position += A

    print(f"day : {day}  달팽이의 위치 : {current_position:5d}미터")

    if current_position >= depth:
        break

    current_position -= B

print(f"우물을 탈출하는데 걸린 날은 {day}일 입니다.")