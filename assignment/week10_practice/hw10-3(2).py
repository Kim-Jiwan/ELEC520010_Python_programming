# 2017110292 김지완

leap_list = [ year for year in range(2001, 2031) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

print(f"2001년부터 2030년 사이의 윤년 : {leap_list}")