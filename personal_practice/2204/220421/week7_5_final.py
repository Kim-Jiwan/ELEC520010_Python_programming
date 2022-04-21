def product_set(set0, set1):
    tmp = set()

    for i in set0:
        for j in set1:
            tmp = tmp.union({(i, j)})
    
    return tmp

def sum_set(tup):
    S = 0

    while isinstance(tup, tuple):
        S += tup[0]
        tup = tup[1]
    else:
        S += tup

    return S

def dice_sum_set(set0, n):
    tmp = set()

    for tup in set0:
        tmp.add(sum_set_recursive(tup, n))

    return tmp

def sum_set_recursive(tup, n):
    
    if n == 2:
        return sum(tup)
    else:
        return tup[0] + sum_set_recursive(tup[1], n - 1)

dice_cases = {1, 2, 3, 4, 5, 6}
dice_cases_2times = product_set(dice_cases, dice_cases)
dice_cases_3times = product_set(dice_cases, dice_cases_2times)
dice_cases_4times = product_set(dice_cases, dice_cases_3times)
dice_cases_5times = product_set(dice_cases, dice_cases_4times)

dice_case = { 2 : dice_cases_2times, 3 : dice_cases_3times, 4 : dice_cases_4times }

dice_sum_4times = dice_sum_set(dice_cases_4times, 4)

for key in dice_case:
    print(dice_sum_set(dice_case[key], key))