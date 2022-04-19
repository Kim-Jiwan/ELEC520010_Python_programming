sales_tuple = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)
sales_decrease_cnt = 0

print(f"일일 매출 기록 : {sales_tuple}")

for i in range(len(sales_tuple) - 1):
    if sales_tuple[i] > sales_tuple[i + 1]:
        sales_decrease_cnt += 1

print(f"지난 {len(sales_tuple)}일 동안 전일대비 매출이 감소한 날은 {sales_decrease_cnt}입니다.")
