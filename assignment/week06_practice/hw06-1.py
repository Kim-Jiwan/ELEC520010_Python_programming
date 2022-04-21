# 2017110292 김지완

menu_table = {"Americano" : 3000, "Ice Americano" : 3500, "Cappuccino" : 4000, "Cafe Latte" : 4500, "Espresso" : 3600}

for key in menu_table:
    print(f"{key:16s}가격 : {menu_table[key]:,}원")

menu = input("위의 메뉴중 하나를 선택하세요 : ")

if menu in menu_table.keys():
    print(f"{menu}는 {menu_table[menu]:,}원 입니다. 결제해주세영~.")
else:
    print(f"엥? {menu}는 메뉴에 없는데요 ㅋ")