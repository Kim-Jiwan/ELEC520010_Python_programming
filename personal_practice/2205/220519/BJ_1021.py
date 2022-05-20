def dequeue():
    global queue
    global N

    queue = queue[1::]
    N -= 1

def left_shift():
    global cnt
    global queue

    tmp = queue[1::]
    tmp.append(queue[0])
    cnt += 1
    queue = tmp

def mul_left_shift(N):
    for _ in range(N):
        left_shift()

def right_shift():
    global cnt
    global queue

    tmp = queue[:-1]
    tmp.insert(0, queue[-1])
    cnt += 1
    queue = tmp


def mul_right_shift(N):
    for _ in range(N):
        right_shift()

N, M = map(int, input().split())
queue = [ i for i in range(1, N + 1) ]
cnt = 0

n_list = list(map(int, input().split()))

for num in n_list:
    if queue.index(num) <= N // 2:
        mul_left_shift(queue.index(num))
        dequeue()
    else:
        mul_right_shift(N - queue.index(num))
        dequeue()

print(cnt)