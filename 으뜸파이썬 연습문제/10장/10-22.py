def score_info(alist):
    total_stud = len(alist) // 3
    valid_stud = 0
    valid_scores = []

    score_iter = iter(alist)

    for _ in range(total_stud):
        tmp = []
        
        for _ in range(3):
            tmp.append(next(score_iter))

        if 0 not in tmp:
            valid_stud += 1
            valid_scores.append(tmp)

    print(f"전체 학생의 수는 {total_stud}명입니다.")
    print(f"유효 점수 획득 학생의 수는 {valid_stud}명입니다.")
    print(valid_scores)

scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 90, 0, 90, 100, 75, 20, 30, 50, 90]

score_info(scores)