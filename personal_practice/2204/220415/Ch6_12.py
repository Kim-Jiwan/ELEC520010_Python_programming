given_list = [5, 6, 3, 9, 2, 12, 3, 8, 7]
given_list_sort = [5, 6, 31, 9, 2, 12 ,13 ,8, 7]

for i in range(len(given_list) - 1):
    if given_list[i] > given_list[i + 1]:
        given_list[i], given_list[i + 1] = given_list[i + 1], given_list[i]

print(given_list)

# 버블 정렬 k개의 요소 중 가장 큰 수를 뒤로 옮기고, k - 1개의 요소에 대해 반복...
for i in range(len(given_list) - 1):
    for j in range(len(given_list) - 1 - i):
        if given_list[j] > given_list[j + 1]:
            given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]

print(given_list)

for i in range(len(given_list_sort) - 1):
    for j in range(len(given_list_sort) - 1 - i):
        if given_list_sort[j] > given_list_sort[j + 1]:
            given_list_sort[j], given_list_sort[j + 1] = given_list_sort[j + 1], given_list_sort[j]

    print(f"{i + 1} 단계 : {given_list_sort[0 : len(given_list_sort) - i - 1]}, {given_list_sort[len(given_list_sort) - i - 1 : len(given_list_sort)]}")