def greet(*names):

    return names

name = greet(1, 2, 3, 5, 6)
namee = ["1", "2", "3", "4", "5"]
dicti = {1 : "a", 2 : "b"}
print(dicti.pop(1))

print(dicti)

print(name.index(3))
print(", ".join(namee))
print("hobby".find("o"))
print("hobby".find("x"))

a = [10, 20, 30]
b = [40, 50, 60]

val = list(zip(a, b))
print(val)

string = 'abcde'

print(string.index("e"), string.find("e"))
print(namee.index("4"), namee.find("4")) # 시퀀스 자료형은 find를 쓸 수 없다