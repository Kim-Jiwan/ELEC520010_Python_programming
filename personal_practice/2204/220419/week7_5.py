def product_set(set0, set1):
    tups = set()

    for i in set0:
        for j in set1:
            # tups = tups | {(i, j)}
            tups = tups.union({(i, j)})

    return tups

def sum_set(set0):
    S = 0

    while isinstance(set0, tuple):
        S += set0[0]
        set0 = set0[1]
    else:
        S += set0

    return S

dice_cases = {1, 2, 3, 4, 5, 6}
dice_cases_2times = product_set(dice_cases, dice_cases)
dice_cases_3times = product_set(dice_cases, dice_cases_2times)
set_sum = set()

for tup in dice_cases_3times:
    set_sum.add(sum_set(tup))

print(set_sum)