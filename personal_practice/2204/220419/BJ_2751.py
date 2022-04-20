import sys

input = sys.stdin.readline

N = int(input())
N_list = []

for i in range(N):
    num = int(input())
    N_list.append(num)

N_list.sort()

for i in range(N):
    print(N_list[i])