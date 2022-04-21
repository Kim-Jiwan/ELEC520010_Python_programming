N, K = map(int, input().split())

jose_list = list(range(1, N + 1))
jose_permu = []

while jose_list: # 빈 list는 False구나! 
    
    # if len(jose_list) == 1 or len(jose_list) == 2:
    if len(jose_list) < K: # 이 case를 잘 처리해야한다..
        tmp = jose_list[K % (len(jose_list)) - 1]
        jose_list.remove(tmp)
    else:
        tmp = jose_list[K - 1]
        jose_list.pop(K - 1)
        jose_list = jose_list[K - 1:] + jose_list[:K - 1]

    jose_permu.append(tmp)

"""print("<", end = "")
for i in range(len(jose_permu)):
    if i != len(jose_permu) - 1:
        print(jose_permu[i], end = ", ")
    else:
        print(jose_permu[i], end = "")
print(">", end = "")"""

print("<", ", ".join(jose_permu), ">", sep = '')
# print(f"<{jose_permu}>")