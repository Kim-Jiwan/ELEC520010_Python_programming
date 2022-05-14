# 2017110292 김지완

class Counter:
    def __init__(self, number = 0):
        if number >= 100 or number <= -1:
            self.__number = 0
        else:
            self.__number = number
    
    def __str__(self):
        return f"C({self.__number})"

    def reset(self):
        self.__number = 0

    def inc(self):
        self.__number += 1

        if self.__number >= 100:
            self.__number = 0

    def dec(self):
        self.__number -= 1

        if self.__number <= -1:
            self.__number = 0

c1 = Counter(10)
c1.inc()
print("c1 = ", c1)

print()

c2 = Counter()
c2.inc()
c2.inc()
c2.dec()
print("c2 = ", c2)
c2.reset()
print("c2 = ", c2)