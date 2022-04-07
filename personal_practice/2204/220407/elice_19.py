N = int(input())
score = []

for _ in range(N):
    score.append(list(map(int, input().split())))

score_sort = sorted(score, reverse = True)

for i in score_sort:
    for j in range(N):
        if i == score[j]:
            print(j + 1, i[0], i[1])