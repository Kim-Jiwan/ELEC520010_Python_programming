student_tuple = (('191101', '카리나', '010-123-45xx'), ('191102', '김민정', '010-223-45xx'), ('191103', '지젤', '010-323-45xx'),('191104', '닝닝', '010-313-34xx') )

student_dict = { number : name for number, name, _ in student_tuple }

number, name, phone = zip(*student_tuple)

student_list = list(zip(number, name, phone))

print(number, name, phone)
print(student_list)

while True:
    number = input("학번을 입력하세요 : ")

    if number in student_dict:
        print(f"{number}학생은 {student_dict[number]}입니다.")
    elif number == "-1":
        print("프로그램을 종료합니다.")
        break
    else:
        print(f"엥? 그런 학생은 저희 그룹에 없는데요?")
