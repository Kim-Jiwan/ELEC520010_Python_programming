src = input("문자를 입력하세요 : ")
print(f"src = {src}")
output = src[0]
count = 0

for char in src:
    if output[-1] == char:
        count += 1
        # 문자의 개수 counting
    else:
        output += str(count) + char
        # count와 char 순서대로 더해줘야합니다. 안그러면 output의 마지막이 숫자로 끝나서
        # 의도한 동작을 하지 않습니다.
        count = 1
        # 새로운 문자 count 초기화

output += str(count)
# 반복문 탈출 후 마지막 문자의 개수 더해줌

print(f"output = {output}")
