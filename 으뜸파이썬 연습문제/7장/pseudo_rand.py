import time as t

def pseudo_rand(x):
    a = 1103515245
    b = 12345

    m = 2 ** 31

    new_x = (a * x + b) % m

    return new_x

# print(pseudo_rand(100))

seed = int(t.time())

for _ in range(5):
    seed = pseudo_rand(seed)
    print(seed)