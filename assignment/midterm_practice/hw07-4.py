list_score = list(input("이름과 국어, 수학, 과학 성적을 입력하세요 : ").split())

# 성적을 정수로 변환, 2, 3, 4 번째에 점수가 등장하므로 i % 4 != 0
for i in range(len(list_score)):
    if i % 4 != 0:
        list_score[i] = int(list_score[i])

list_tuple_score = []

# 4개씩 나눠서 tuple로 저장 후 list에 append
for i in range(len(list_score) // 4):
    list_tuple_score.append(tuple(list_score[4 * i : 4 * i + 4]))

# set tuple
tuple_score = tuple(list_tuple_score)

_, _, math, science = zip(*tuple_score)

math_science_Avg = (sum(math) + sum(science)) / (len(math) + len(science))
# avg = [ (i + j + k) / 3 for _, i, j, k in tuple_score ]
print(math_science_avg)

print(f"학생들의 수학과 과학 성적의 평균은 {math_science_Avg:.2f}입니다.")

student_dict = { name : (k + m + s) / 3 for name, k, m, s in tuple_score }


for key in student_dict.keys():
    print(f"{key}{student_dict[key]:10.2f}")    