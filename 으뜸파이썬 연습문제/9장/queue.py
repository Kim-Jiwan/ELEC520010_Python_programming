import sys

class Queue:
    def __init__(self):
        self.__queue = []

    def __str__(self):
        return f"{self.__queue}"

    def push(self, x):
        self.__queue.append(x)

    def pop(self):
        if self.__queue:
            print(self.__queue.pop(0))
        else:
            print(-1)

    def size(self):
        print(len(self.__queue))

    def empty(self):
        if self.__queue:
            print(0)
        else:
            print(1)

    def front(self):
        if self.__queue:
            print(self.__queue[0])
        else:
            print(-1)

    def back(self):
        if self.__queue:
            print(self.__queue[-1])
        else:
            print(-1)

input = sys.stdin.readline
n = int(input())
queue = Queue()

for _ in range(n):
    intr = input().split()
    
    if intr[0] == "push":
        queue.push(int(intr[1]))
    elif intr[0] == "pop":
        queue.pop()
    elif intr[0] == "size":
        queue.size()
    elif intr[0] == "empty":
        queue.empty()
    elif intr[0] == "front":
        queue.front()
    elif intr[0] == "back":
        queue.back()