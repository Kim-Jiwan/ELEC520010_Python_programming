# 2017110292 김지완

leap_list = [ year for year in filter(lambda x : (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0) , range(2001, 2031)) ]

print(f"2001년부터 2030년 사이의 윤년 : {leap_list}")