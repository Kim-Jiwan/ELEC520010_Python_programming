# 2017110292 김지완
import time

def sum1to1000000():
    S = 0

    for i in range(1, 1000000 + 1):
        S += i

    return S

start_time = time.time()

for i in range(100):
    sum1to1000000()

end_time = time.time()

print(f"1에서 1,000,000까지의 합을 100번 반복해서 구하는 시간 : {end_time - start_time:.5f}")