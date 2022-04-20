factorial = [1, 1, 2]

for i in range(2, 21):
    factorial.append(factorial[i] * (i + 1))

# print(factorial)

def euler(n):
    euler_num = 0

    for i in range(n + 1):
        euler_num += (1 / factorial[i])

    return euler_num

print(f"euler({5:2d}) = {euler(5):10.5f}")
print(f"euler({20:2d}) = {euler(20):10-.5f}")