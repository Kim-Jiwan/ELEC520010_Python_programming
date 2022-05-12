N = int(input())
score_list = list(map(int, input().split()))

score_max = max(score_list)

for i in range(len(score_list)):
    score_list[i] = score_list[i] / score_max * 100

print(sum(score_list) / N)