# 2017110292 김지완

list1 = [1, 2, 3]
list1.remove(list1[-1])
print(list1)

list2 = list(map(lambda x: x + 1, list1))

print(list2)