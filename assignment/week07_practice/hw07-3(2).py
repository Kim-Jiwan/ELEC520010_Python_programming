# 2017110292 김지완
import time

def my_rand(x):
    a = 1103515241
    b = 12343
    m = 1000000

    new_x = (a * x + b) % m

    return new_x

seed = int(time.time())

for _ in range(5):
    seed = my_rand(seed)
    print(seed)