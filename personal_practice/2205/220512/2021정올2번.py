N = int(input())
n_list = list(map(int, input().split()))
cnt = 0
   
S = sum(n_list)

if S % 4 != 0:
    cnt = 0
else:
    tmp_S = 0
    index = 0
    while tmp_S == S // 4:
            