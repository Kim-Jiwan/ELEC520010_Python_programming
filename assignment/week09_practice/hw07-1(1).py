# 2017110292 김지완
import datetime as dt

today = dt.date.today()

start_day = dt.datetime(2019, 2, 24)
time_gap = dt.datetime.now() - start_day

print(f"춘향이와 몽룡이의 연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")
print(f"연애 시작일로부터 결과한 날짜 : {time_gap.days}일")