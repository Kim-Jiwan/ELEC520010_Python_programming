import time as t

def sum1to1000000():
    sum = 0

    for i in range(1, 1000000 + 1):
        sum += i

    return sum

start_time = t.time()

for _ in range(100):
    sum1to1000000()

end_time = t.time()

print(end_time - start_time)