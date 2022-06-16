from turtle import distance


class Circle:
    PI = 3.14
    
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def area(self):
        return self.PI * self.__radius * self.__radius

    def overlaps(self, c):
        if ((self.__x - c.__x) ** 2 + (self.__y - c.__y) ** 2) ** 0.5 >= self.__radius + c.__radius:
            return False
        else:
            return True

    def contains(self, c):
        if ((self.__x - c.__x) ** 2 + (self.__y - c.__y) ** 2) ** 0.5  + c.__radius <= self.__radius:
            return True
        else:
            return False


c1 = Circle(0, 0, 100)
c2 = Circle(0, -10, 10)
c3 = Circle(-100, 0, 120)
c4 = Circle(100, 100, 10)

print(f"c1 overlaps c2 : {c1.overlaps(c2)}")
print(f"c1 overlaps c3 : {c1.overlaps(c3)}")
print(f"c1 overlaps c4 : {c1.overlaps(c4)}")

print(f"c1 contains c2 : {c1.contains(c2)}")
print(f"c1 contains c3 : {c1.contains(c3)}")
print(f"c1 contains c4 : {c1.contains(c4)}")