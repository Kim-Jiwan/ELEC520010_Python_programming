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

def dice_sum_set(set0):
    tmp = set()

    for tup in set0:
        tmp.add(sum_set(tup))

    return tmp

dice_cases = {1, 2, 3, 4, 5, 6}
dice_cases_2times = product_set(dice_cases, dice_cases)
dice_cases_3times = product_set(dice_cases, dice_cases_2times)

dice_sum_4times = dice_sum_set(product_set(dice_cases, dice_cases_3times))

print(dice_sum_4times)
