from email.policy import default


N, M = map(int, input().split())
chess_board = []
cnt = 0

default_chess = ["WBWBWBWB", 
                 "BWBWBWBW", 
                 "WBWBWBWB",
                 "BWBWBWBW", 
                 "WBWBWBWB", 
                 "BWBWBWBW",
                 "WBWBWBWB",
                 "BWBWBWBW" ]
                 
# 이거 convolution이네!!!!!

for _ in range(N):
    chess_board.append(input())




print(cnt)