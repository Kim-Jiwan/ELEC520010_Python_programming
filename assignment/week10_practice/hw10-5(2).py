# 2017110292 김지완

print([ n for n in range(10, 51) if (n % 2 == 1) and (all(n % m for m in range(3, n, 2))) ])