def distance(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

class Circle:
    PI = 3.14

    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __str__(self):
        return f"Circle : (x = {self.__x}, y = {self.__y}, r = {self.__radius}), 면적 : {Circle.PI * self.__radius ** 2}"

    # setters
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_radius(self, radius):
        self.__radius = radius

    # getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_radius(self):
        return self.__radius

    def area(self):
        return Circle.PI * self.__radius ** 2


    def overlap(self, r):
        if distance(self.__x, r.__x, self.__y, r.__y) >= self.__radius + r.__radius:
            return False
        else:
            return True

    def contain(self, r):
        if distance(self.__x, r.__x, self.__y, r.__y) <= self.__radius - r.__radius and self.__radius >= r.__radius:
            return True
        else:
            return False

c1 = Circle(0, 0, 100)
c2 = Circle(0, -10, 10)
c3 = Circle(-100, 0, 120)
c4 = Circle(100, 100, 1)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c3 = {c3}")

print(f"c1 contain c2 : {c1.contain(c2)}")
print(f"c1 contain c3 : {c1.contain(c3)}")
print(f"c1 contian c4 : {c1.contain(c4)}")
print(f"c2 contian c1 : {c2.contain(c1)}")

print(f"c1 overlaps c2 : {c1.overlap(c2)}")
print(f"c1 overlaps c3 : {c1.overlap(c3)}")