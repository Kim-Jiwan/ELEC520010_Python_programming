def product_set(set1, set2):
    res = set()

    for i in set1:
        for j in set2:
            res = res | {(i, j)} # {(i, j)} 자체가 set
    
    return res

def sum_set_recursive(tup, n):
    sum_of_set = 0
    
    if n == 2:
        sum_of_set = sum(tup)
    else:
        sum_of_set = tup[0] + sum_set_recursive(tup[1], n - 1)
        
    return sum_of_set

dice_cases = {1, 2, 3, 4, 5, 6}
dice_cases_2times = product_set(dice_cases, dice_cases)
dice_cases_3times = product_set(dice_cases, dice_cases_2times)
dice_cases_4times = product_set(dice_cases, dice_cases_3times)
dice_cases_5times = product_set(dice_cases, dice_cases_4times)

# print(dice_cases_3times)


set_sum = { sum_set_recursive(tup, 3) for tup in dice_cases_3times }
set_sum4 = { sum_set_recursive(tup, 4) for tup in dice_cases_4times }
set_sum5 = { sum_set_recursive(tup, 5) for tup in dice_cases_5times }

print(set_sum)
print(set_sum4)
print(set_sum5)