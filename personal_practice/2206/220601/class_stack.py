class stack:
    def __init__(self, stack = []):
        self.__stack = stack

    def __str__(self):
        return f"{self.__stack}"

    def push(self, element):
        self.__stack.append(element)
        print(f"{self.__stack}")

    def pop(self):
        self.__stack.pop()

stack_0 = stack()
stack_0.push(1)

print(stack_0)