def queueing(queue, K):
    if len(queue) >= K:
        return queue[K - 1::] + queue[0:K - 1]
    else:
        return queue[K % len(queue) - 1::] + queue[0:K % len(queue) - 1]

N, K = map(int, input().split())
queue = [ i for i in range(1, N + 1) ]
josephus_permu = []

# 요세푸스 순열 채우기 dequeue로 부터 값을 받는다.
while queue:
    queue = queueing(queue, K)
    josephus_permu.append(queue.pop(0))

# 출력 formatting
for i in range(len(josephus_permu)):
    josephus_permu[i] = str(josephus_permu[i])

print("<" + ", ".join(josephus_permu) + ">")

