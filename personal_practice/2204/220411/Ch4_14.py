def sort3(num1, num2, num3):
    sort_lsit = []
    sort_lsit.append(num1)
    sort_lsit.append(num2)
    sort_lsit.append(num3)
    sort_lsit.sort()

    return sort_lsit

print("세 수를 입력하세요 : ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

sort_list = sort3(num1, num2, num3)

print(f"정렬된 리스트는 다음과 같습니다 : {sort_list[0]} {sort_list[1]} {sort_list[2]}")