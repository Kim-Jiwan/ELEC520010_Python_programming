# 2017110292 김지완

student_tuple = (('191101', '카리나', '010-123-45xx'), ('191102', '김민정', '010-223-45xx'), ('191103', '지젤', '010-323-45xx'),('191104', '닝닝', '010-313-34xx'))
student_dic = {num:name for num, name, phone in student_tuple}

print(f"학생 정보 : {student_dic}")

while True:
    num = input("학번을 입력하세요 : ")

    if num in student_dic.keys():
        print(f"{num}번 학생은 {student_dic[num]}입니다.")
    elif num == "-1":
        print("프로그램을 종료합니다.")
        break
    else:
        print("엥? 그런 학생은 저희 그룹에 없는데요 ㅋ.")