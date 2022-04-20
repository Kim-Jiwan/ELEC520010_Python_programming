src = input("문자를 입력하세요 : ")
output = src[0]
cnt = 0

for char in src:
    if char == output[-1]:
        cnt += 1
    else:
        output += str(cnt) + char
        cnt = 1
output += str(cnt)

print(f"src = {src}")
print(f"output = {output}")