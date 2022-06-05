import datetime as dt

today = dt.datetime.now()
xMAS = dt.datetime(2022, 12, 25)

# dt.date.today()는 년, 월, 일 만 지원하는 구나!! 시간정보는 제공하지 않는다.
time_gap = xMAS - today
# 빼면 timedelta class가 되는구나!!

print(f"{time_gap.days}일")
# days는 timedelta class의 자료형

# print(f"{time_gap.days}일, {time_gap.seconds // 3600}시간")

start_day = dt.datetime(2022, 2, 24)

print(f"연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")

time_gap = dt.datetime.now() - start_day

print(f"{time_gap.days}일")

deltas = [100, 200, 500, 1000]

for delta in deltas:
    tmp = dt.timedelta(days = delta)
    time = dt.datetime.now() + tmp

    print(f"{delta}일 기념일 : {time.year}년 {time.month}월 {time.day}일")