print("사전 프로그램 시작... 종료는 q를 입력")
my_dict = {}

while True:
    instr = input("$ ")

    if instr == 'q':
        break
    else:
        if instr[0] == '<':
            key, val = instr[1::].split(":")
            my_dict[key] = val

        if instr[0] == '>':
            if instr[1::] in my_dict.keys():
                print(f"{my_dict[instr[1::]]}")
            else:
                print(f"{instr[1::]}가 사전에 없습니다.")

        elif instr[0] != '<' and instr[0] != '>':
            print("입오류가 발생했습니다.")