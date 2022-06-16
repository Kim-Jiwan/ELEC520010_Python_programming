# 2017110292 김지완

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

my_dog = Dog("Mango", 3)

print(Dog)
print(f"my_dog의 이름은 {my_dog.__name}이고, 나이는 {my_dog.__age}살입니다.")
# __name은 외부에서 접근할 수 없다!!!!