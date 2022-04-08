A, B = map(int, input().split())
mul_strange = 0
A_list, B_list = [], []

while A != 0:
    A_list.append(A % 10)

    A //= 10

while B != 0:
    B_list.append(B % 10)

    B //= 10

"""
for i in A_list:
    for j in B_list:
        if i != 0 and j != 0:
            mul_strange += i * j
"""

mul_strange = sum(A_list) * sum(B_list) # 분배법칙이다..!
# 코드 최적화 -> 간단한 수학으로 반복문 줄이기

print(mul_strange)