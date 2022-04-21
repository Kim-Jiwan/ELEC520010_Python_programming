def greet(*names):
    names[0] = 10

    print(names)

greet(1, 2, 3, 5, 6)