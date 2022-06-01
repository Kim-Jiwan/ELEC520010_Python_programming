def first_odd(iter):
    for num in iter:
        if num % 2 == 1:
            return num

numbers = [2, 8, 6, 4, 3, 1, 4, 6, 2]

print(f"처음으로 나타나는 홀수는 : {first_odd(iter(numbers))}")