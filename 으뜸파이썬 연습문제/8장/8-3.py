f = open("hello.txt", 'a')

f.write("Welcome to the python!.\n")
f.close()

f = open("hello.txt", "r")

s = f.readline().rstrip()

while s:
    print(s)
    s = f.readline().rstrip()

f.close()