scores = list(input("이름, 국어, 수학, 과학: ").split())
scores_tups = []

for i in range(len(scores)):
    if i % 4 != 0:
        scores[i] = int(scores[i])

for i in range(len(scores) // 4):
    scores_tups.append(tuple(scores[4 * i:4 * i + 4]))

_, _, math, science = zip(*scores_tups)

print(f"학생들의 수학과 과학 성적의 평균은 각각 {sum(math) / len(math)}점, {sum(science) / len(science)}점 입니다.")

print("이름         평균성적")

student_dict = { name : (k + m + s) / 3 for name, k, m, s in scores_tups }

for key in student_dict:
    print(f"{key}{student_dict[key]:15.2f}")