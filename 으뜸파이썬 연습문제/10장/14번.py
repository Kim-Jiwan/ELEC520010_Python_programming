fruits = { "Apple" : "사과", "Strawberry" : "딸기", "Peach" : "복숭아", "Grape" : "포도" }

fruits_list_1 = [ char for char in map(lambda fruits : f"{fruits[0]} = {fruits[1]}", fruits.items()) ]
fruits_list_2 = [ f"{fruit[0]} = {fruit[1]}" for fruit in fruits.items() ]
print(fruits_list_1)
print(fruits_list_2)