# 2017110292 김지완

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Mango", 3)

print(Dog)
print(f"my_dog의 이름은 {my_dog.name}이고, 나이는 {my_dog.age}살입니다.")