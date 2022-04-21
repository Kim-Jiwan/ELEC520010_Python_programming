menu_dict = { "Americano":3000, "Ice Americano":3500, "Cappuccino":4000, "Cafe Latte":4500, "Espresso":3600 }

for key in menu_dict:
    print(f"{key:15s}     가격 : {menu_dict[key]:,}원")

while True:
    menu = input("위의 메뉴중 하나를 선택하세요 : ")

    if menu in menu_dict:
        print(f"{menu}는 {menu_dict[key]:,}원 입니다.")
    else:
        print("fuck you")
        break