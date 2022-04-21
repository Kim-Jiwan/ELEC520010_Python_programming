N, M = map(int, input().split())
# 듣도 못한 사람 : N, 보도 못한 사람 : M
# 둘때 줄부터 N개의 줄에 걸쳐 듣도 못한 사람
# N + 2째 줄 부터 보도 못한 사람
deutbo_set = set()
deut_set = set()
bo_set = set()

for i in range(N + M):
    name = input()

    if i < N:
        deut_set.add(name)
    else:
        bo_set.add(name)

deutbo_list = list(deut_set.intersection(bo_set))
deutbo_list.sort()

print(len(deutbo_list))

for deutbo in deutbo_list:
    print(deutbo)