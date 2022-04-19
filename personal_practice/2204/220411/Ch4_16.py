def sort_string(inputList):

    int_list = [ int(val) for val in inputList ]
    # print(int_list)

    int_list.sort()

    return int_list

inputStr = input("쉼표로 구분된 정수를 여러 개 입력하시오: ")
inputList = inputStr.split(",")

print(f"입력된 정수의 리스트 : {inputList}")
print("정렬된 정수의 리스트 : ", end = '')

for i in sort_string(inputList):
    print(i, end = " ")