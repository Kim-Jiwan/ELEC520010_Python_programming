num = int(input("1에서 9사이의 수를 입력하세요 : "))

while not(num > 1 and num < 10):
    num = int(input("1에서 9사이의 수를 다시 입력하세요 : "))

for i in range(1, 10):
    print(f"{num:2d} * {i:2d} = {num * i:2d}")