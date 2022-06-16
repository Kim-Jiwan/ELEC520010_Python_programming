def creat_gen():
    alist = range(1, 4)

    for x in alist:
        yield x

my_gerator = creat_gen()

for x in my_gerator:
    print(x)

for x in my_gerator:
    print(x)