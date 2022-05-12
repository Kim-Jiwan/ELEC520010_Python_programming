# 2017110292 김지완
try:
    f = open("greet.txt", "x")
    f.write("Hi, everyone.\n")
    f.write("Welcome to Python.")
    f.close()
    
except Exception as e :
    print("쓰기 금지 모드 입니다.")
    print(f"Error : {e}")