length = [0, 1, 1, 2]

for i in range(3, 80):
    length.append(length[i] + length[i-1])

# fibonacci sequences define

N = int(input())
rouNd = 0

if N == 1:
    rouNd = 4
elif N == 2:
    rouNd = 6
elif N == 3:
    rouNd = 10
elif N >= 4:
    rouNd = length[N] * 3 + length[N-1] * 2 + length[N-2] * 2 + length[N-3]

print(rouNd)