def reverse_generator(alist):

    for x in sorted(alist, reverse = True):
        yield x

def last_odd(alist):
    tmp_generator = reverse_generator(alist)

    for x in tmp_generator:
        if x % 2 == 1:
            return x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16]

print(f"마지막 홀수는 : {last_odd(numbers)}")