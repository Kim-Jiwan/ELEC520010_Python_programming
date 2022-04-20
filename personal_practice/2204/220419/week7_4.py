scores = list(input("이름과 국어, 수학, 과학 성적을 입력하세요 : ").split())
scores_tup = []

for i in range(len(scores)):
    if i % 4 != 0:
        scores[i] = int(scores[i])

for i in range(0, len(scores), 4):
    scores_tup.append((scores[i], scores[i + 1], scores[i + 2], scores[i + 3]))

# set tuple
scores_tup = tuple(scores_tup)

_, _, math, science = zip(*scores_tup)

print(f"학생들의 수학과 과학 성적의 평균은 {sum(math) / len(math)}, {sum(science) / len(science)} 입니다.")

student_dict = { name : (k + m + s) / 3 for name, k, m ,s in scores_tup }

print("이름      평균성적")
print("------------------")
for key in student_dict.keys():
    print(f"{key}{student_dict[key]:12.2f}")