N = int(input())

for _ in range(N):
    score = 0
    S = 0

    quiz_answer = input()

    for answer in quiz_answer:
        if answer == "O":
            S += 1
            score += S
        elif answer == "X":
            S = 0

    print(score)