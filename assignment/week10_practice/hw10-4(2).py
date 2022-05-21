# 2017110292 김지완

def reverse_generator(n_list):
    for num in sorted(n_list, reverse = True):
        yield num

def last_odd(n_list):
    # 10-4(1)애서 구현한 reverse_generator() 호출
    reverse_iterator = reverse_generator(n_list)

    # reverse iterator에서 제일 먼저 나타나는 홀수를 return하면 리스트의 가장 마지막에 나타나는 홀수를 return한다.
    for num in reverse_iterator:
        if num % 2 == 1:
            return num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 ,16]

print(f"마지막 홀수는 : {last_odd(numbers)}")