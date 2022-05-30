# 시발!!!!!!!!!!!

str1 = "WBWBWBWB"
str2 = "BWBWBWBW"

chess_default_1 = [str1, str2, str1, str2, str1, str2, str1, str2]
chess_default_2 = [str2, str1, str2, str1, str2, str1, str2, str1]

N, M = map(int, input().split())

chess = []
tmp = float("inf")


for _ in range(N):
    chess.append(input())

for i in range(N - 7):
    matrix_tmp = chess[i:i+8]
    for j in range(M - 7):
        matrix = [ char[j:j+8] for char in matrix_tmp ]
        cnt = 0

        if matrix[0][0] == "W":
            for k in range(7):
                for l in range(7):
                    if matrix[i][j] != chess_default_1[i][j]:
                        cnt += 1
                    tmp = min(tmp, cnt)

            cnt = 0
            
        elif matrix[0][0] == "B":
            for k in range(7):
                for l in range(7):
                    if matrix[i][j] != chess_default_2[i][j]:
                        cnt += 1
                    tmp = min(tmp, cnt)
        
print(tmp)