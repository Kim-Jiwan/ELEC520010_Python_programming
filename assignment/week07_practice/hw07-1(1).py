# 2017110292 김지완
import datetime as dt
from tracemalloc import start

# data class -> 날짜만 표시
# datatime class -> 날짜, 시분초 까지 표시

today = dt.date.today()
start_day2 = dt.date(2020, 10, 10)
gap = today - start_day2 # 얘도 timedelta

start_day = dt.datetime(2019, 2, 24, 21, 10, 1)
time_gap = dt.datetime.now() - start_day # 빼는 순간 timedelta class가 된다.

print(type(time_gap))
print(type(gap))


print(f"춘향이와 몽룡이의 연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")
print(f"연애 시작일로부터 결과한 날짜 : {gap.days}일")