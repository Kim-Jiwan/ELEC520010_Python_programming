class Rectangle:
    PI = 3.14

    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle : (x = {self.__x}, y = {self.__y}, w = {self.__width}, h = {self.__height}, 면적 : {self.area()})"

    def area(self):
        return self.__width * self.__height

    def overlaps(self, r):
        if r.__x > self.__x and r.__x - self.__x >= self.__width:
            return False
        elif r.__x < self.__x and self.__x - r.__x >= r.__width:
            return False
        elif r.__y > self.__y and r.__y - self.__y >= r.__height:
            return False
        elif r.__y < self.__y and self.__y - r.__y >= self.__height:
            return False
        else:
            return True

    # True False를 판단할때 나만의 팁
    # 사건의 조건과 여사건의 조건 중 어떤 조건이 기술하기 쉬운지 판단해보고
    # 더 쉬운 조건을 if문에 기술하고 반대 case는 else로 처리
    def contains(self, r):
        if (self.__width >= abs(r.__x - self.__x) + r.__width) and (self.__height >= abs(r.__y - self.__y) + r.__height):
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

r4 = Rectangle(0, 100, 100, 100)
r5 = Rectangle(-100, 100, 1000, 1000)

print(r1)
print(r2)
print(r3)

print(f"r1 contains r2 : {r1.contains(r2)}")
print(f"r1 contains r5 : {r1.contains(r5)}")
print(f"r1 overlaps r2 : {r1.overlaps(r2)}")
print(f"r1 overlaps r5 : {r1.overlaps(r5)}")

print(f"\nr1 overlaps r4 : {r1.overlaps(r4)}")
print(f"\nr1 overlaps r5 : {r1.overlaps(r5)}")

print(f"{r1.__dict__}")