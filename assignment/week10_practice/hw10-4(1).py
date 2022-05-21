# 2017110292 김지완

def reverse_generator(n_list):
    for num in sorted(n_list, reverse = True):
        yield num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 ,16]

# 문제에서 generator명과 반복자 변수명이 헷갈려서 둘다 작성했습니다.
for num in reverse_generator(numbers):
    print(num, end = " ")

my_reverse_iterator = reverse_generator(numbers)

print()

for num in my_reverse_iterator:
    print(num, end = " ")

# my_reverse_iterator 재실행시 반환 X
for num in my_reverse_iterator:
    print(num, end = " ")