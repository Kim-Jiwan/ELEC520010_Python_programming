N = int(input())
dungchi_list = []

for i in range(N):
    x, y = map(int, input().split())
    # x : 몸무게, y : 키
    
    dungchi_list.append((x, y)) # 튜플로 몸무게, 키 추가

dungchi_rank_list = [ 1 ] * len(dungchi_list)

for i in range(len(dungchi_list)):
    tmp = dungchi_list[:i] + dungchi_list[i + 1:]

    for dungchi in tmp:
        if dungchi[0] > dungchi_list[i][0] and dungchi[1] > dungchi_list[i][1]:
            dungchi_rank_list[i] += 1

for rank in dungchi_rank_list:
    print(rank, end = " ")