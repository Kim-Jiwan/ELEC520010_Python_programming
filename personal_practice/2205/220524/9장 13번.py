class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle : (x = {self.__x}, y = {self.__y}, w = {self.__width}, h = {self.__height}), 면적 : {self.__width * self.__height}"
    
    # below are setters
    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    # below are getters
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self): 
        return self.__width * self.__height

    def overlap(self, r):
        if self.__x > r.__x or self.__y > r.__y:
            if self.__y - r.__y > self.__height or self.__x - r.__x > self.__width:
                return False
            else:
                return True
        else:
            if self.__y - r.__y <= self.__height or self.__x - r.__x <= self.__width:
                return False
            else:
                return True

    def contain(self, r):
        if self.__x <= r.__x and self.__y >= r.__y and self.__height >= r.__height and self.__width >= r.__width:
            return True
        else:
            return False

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print(f"r1 = {r1}")
print(f"r2 = {r2}")
print(f"r3 = {r3}")

print(f"r1 contains r2 : {r1.contain(r2)}")
print(f"r1 contains r3 : {r1.contain(r3)}")
print(f"r1 overlap r2 : {r1.overlap(r2)}")
print(f"r1 overlap r3 : {r1.overlap(r3)}")