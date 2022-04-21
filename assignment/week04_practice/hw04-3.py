# 2017110292 김지완

def sum_range(n1, n2):
    s = 0

    for i in range(n1, n2 + 1):
        s += i

    return s

print("{:3d}에서 {:3d}까지의 정수의 합 : {:4d}".format(10, 20, sum_range(10, 20)))
print("{:3d}에서 {:3d}까지의 정수의 합 : {:4d}".format(40, 100, sum_range(40, 100)))