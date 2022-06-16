# 2017110292 김지완
open_mode = input()

try:
    f = open("greet.txt", open_mode)
    f.write("Hi, everyone.\n")
    f.write("Welcome to Python.")
    f.close()
    
except Exception as e :
    print("쓰기 금지 모드 입니다.")
    print(f"Error : {e}")