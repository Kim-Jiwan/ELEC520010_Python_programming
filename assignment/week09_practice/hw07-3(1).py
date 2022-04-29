# 2017110292 김지완
import time

def my_rand(x):
    a = 1103515241
    b = 12343
    m = 1000000

    new_x = (a * x + b) % m

    return new_x

X = 16234 # 똑같은 seed값에서는 똑같은 값이 나온다.
# seed를 고정하면 외부변수에 영향을 받지 않는다.

for _ in range(10):
    X = my_rand(X)
    print(X)