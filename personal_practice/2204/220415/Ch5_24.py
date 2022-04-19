# 어떤 정수 n의 약수들 중에서 n을 제외한 나머지 약수(진약수)의 합이 n이 되는 수
# 진약수의 합이 n이 되는 수를 완전수라고 한다.

def complete_number(num):
    real_divisor = []

    if num % 2 == 1:
        for i in range(1, num // 2, 2):
            if num % i == 0:
                real_divisor.append(i)

    else:
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                real_divisor.append(i)

    return real_divisor

for i in range(1, 10001):
    if sum(complete_number(i)) == i:
        print(f"{i}은 완전수입니다.")
        print(f"{i}의 약수 : {complete_number(i)}, 약수의 합 : {sum(complete_number(i))}")