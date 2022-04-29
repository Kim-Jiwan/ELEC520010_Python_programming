# 모든 학생에게 똑같이 나눠주고 남아있는 사과의 수를 최소

N = int(input())
apple_remainder = 0

for _ in range(N):
    stduents, apples = map(int, input().split())

    apple_remainder += apples % stduents

print(apple_remainder)