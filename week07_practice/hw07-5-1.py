def product_set(set1, set2):
    res = set()

    for i in set1:
        for j in set2:
            res = res | {(i, j)} # {(i, j)} 자체가 set
    
    return res

dice_cases = {1, 2, 3, 4, 5, 6}
dice_cases_2times = product_set(dice_cases, dice_cases)
dice_cases_3times = product_set(dice_cases, dice_cases_2times)
dice_cases_4times = product_set(dice_cases, dice_cases_3times)
sum_set_3 = set()
sum_set_4 = set()

for tup in dice_cases_4times:
    s = 0
    tmp = tup
    while isinstance(tmp, tuple):
        s += tmp[0]
        tmp = tmp[1]
    else:
        s += tmp
        
    sum_set_4.add(s)

for tup in dice_cases_3times:
    s = 0
    tmp = tup
    while isinstance(tmp, tuple):
        s += tmp[0]
        tmp = tmp[1]
    else:
        s += tmp
        
    sum_set_3.add(s)
        
print(sum_set_3)
print(sum_set_4)