tup = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
dep = set()

for data in tup:
    if tup.count(data) > 1:
        dep = dep | {data, }

print(dep)