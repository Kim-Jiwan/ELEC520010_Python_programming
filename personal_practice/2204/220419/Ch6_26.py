mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

tup = list(map(int, input("두 값을 입력하세요 : ").split()))
tup_rev = tup
tup = tuple(tup)
flag = 0

for i in range(len(mylist)):
    if tup == mylist[i]:
        print(f"{i + 1}번째에 {tup} 요소가 있습니다.")
        flag = 1

tup_rev.reverse()
tup_rev = tuple(tup_rev)

if flag == 0:
    for i in range(len(mylist)):
        if tup_rev == mylist[i]:
            print(f"{tup} 요소는 없으나 {i + 1}번째에 {tup_rev} 요소가 있습니다.")
            flag = 1

if flag == 0:
    print("이 요소는 없습니다.")