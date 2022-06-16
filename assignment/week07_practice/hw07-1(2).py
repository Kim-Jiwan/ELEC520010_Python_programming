# 2017110292 김지완
import datetime as dt

# def day_after(start_day, n):
#     date = start_day + dt.timedelta(days = n) # 이건 또 datetime이네..!!
#     print(f"{n:4d}일 기념일 : {date.year:4d}년 {date.month:2d}월 {date.day:2d}일")

# start_day = dt.datetime(2019, 2, 24)

# print(f"춘향이와 몽룡이의 연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")
# day_after(start_day, 100)
# day_after(start_day, 200)
# day_after(start_day, 500)
# day_after(start_day, 1000)

def days_after(start, n):
    date = start + dt.timedelta(days = n) # timedelta는 date, datetime 둘다 쓸수있다!!

    print(f"{n:4d}일 기념일 : {date.year:4d}년 {date.month:2d}월 {date.day:2d}일")

start = dt.date(2020, 10, 12)

days_after(start, 100)
days_after(start, 500)
days_after(start, 600)