try:
    f = open("greet.txt", "x")

    f.write("Hi, everyone.\n")
    f.write("Welcome to Python.\n")

except:
    print("쓰기 금지 모드입니다.")