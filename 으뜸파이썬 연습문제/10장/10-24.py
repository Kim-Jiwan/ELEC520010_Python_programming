a = [(2, 5), (1, 4), (4, 7), (2, 3), (2, 1)]

b = sorted(a, key = lambda x : x[0])
c = sorted(a, reverse = True, key = lambda x : x[1])

print(b)
print(c)