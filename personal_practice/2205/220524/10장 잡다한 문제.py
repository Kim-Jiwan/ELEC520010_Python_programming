# 10장 6번
n_list = [ 44, 66, 34, 24, 144, 98, 38, 568, 234, 345 ]

new_list = [ num for num in filter(lambda x : x % 12 == 0, n_list) ]
new_list1 = [ num for num in n_list if num % 12 == 0 ]

print(new_list)
print(new_list1)

# 10장 7번
n_list_7 = [ -22.3, 29.44, 902.2, 45.7, -887.1, -56.3 ]

new_list_7 = [ num for num in map(int, filter(lambda x : x > 0, n_list_7)) ]
new_list_abbreviation = [ int(num) for num in n_list_7 if num > 0 ]

print(new_list_7)
print(new_list_abbreviation)


# 10장 8번
from functools import reduce

n_list_8 = [ -22.3, 29.44, 902.2, 45.7, -887.1, -56.3 ]
n_max = reduce(lambda a, b : int(a) if a > b else int(b), n_list_8)
n_min = reduce(lambda x, y : int(x) if x < y else int(y), n_list_8)

print(n_max, n_min)

# 10장 10번
n_list_10 = list(range(1, 101))
new_list_10_1 = [ num for num in filter(lambda x : x % 6 == 0 and x % 7 == 0, n_list_10) ]
new_list_10_2 = [ num for num in n_list_10 if num % 6 == 0 and num % 7 == 0 ]

print(new_list_10_1, new_list_10_2)

# 10장 11번
char_list_11 = [ "one", "two", "three", "four" ]
new_list_11_1 = [ char for char in map(lambda c : c[0].upper() + c[1::], char_list_11) ]
new_list_11_2 = [ char[0].upper() + char[1::] for char in char_list_11]

print(new_list_11_1, new_list_11_2)

# 10장 12번 
char_list_12 = [ "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday" ]
new_list_12_1 = [ char for char in map(lambda c : c[0:3].upper(), char_list_12) ]
new_list_12_2 = [ char[0:3].upper() for char in char_list_12 ]

print(new_list_12_1, new_list_12_2)

# 10장 14번
fruits = { "Apple" : "사과", "Strawberry" : "딸기", "Peach" : "복숭아", "Grape" : "포도" }

fruits_list_1 = [ char for char in map(lambda fruits : f"{fruits[0]} = {fruits[1]}", fruits.items()) ]
fruits_list_2 = [ f"{fruit[0]} = {fruit[1]}" for fruit in fruits.items() ]
print(fruits_list_1)
print(fruits_list_2)