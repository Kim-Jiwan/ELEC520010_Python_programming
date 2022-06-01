fruits = { "Apple" : "사과", "Strawberry" : "딸기", "Peach" : "복숭아", "Grape" : "포도" }

fruits_list_1 = [ char for char in map(lambda fruits : f"{fruits[0]} = {fruits[1]}", fruits.items()) ]
fruits_list_2 = [ f"{fruit[0]} = {fruit[1]}" for fruit in fruits.items() ]

fruits_tup_list = [ (fruit.split(" = ")[0], fruit.split(" = ")[1]) for fruit in fruits_list_1 ]

fruits_1 = dict((y, x) for x, y in fruits_tup_list)

print(fruits_tup_list)
print(fruits_1)