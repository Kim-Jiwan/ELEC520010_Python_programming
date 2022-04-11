def product_set(set1, set2):
    res = set()

    for i in set1:
        for j in set2:
            res = res | {(i, j)} # {(i, j)} 자체가 set
    
    return res

def sum_set_recursive(tup, n):

    sum_set = 0

    if n == 2:
        sum_set = sum(tup)
    else:
        sum_set = tup[0] + sum_set_recursive(tup[1], n - 1)

    return sum_set

cases = { 1, 2, 3, 4, 5, 6 }
cases_2times = product_set(cases, cases)
cases_3times = product_set(cases, cases_2times)
cases_4times = product_set(cases, cases_3times)
cases_5times = product_set(cases, cases_4times)

# print(cases_3times)

sum_set2 = { sum(tup) for tup in cases_2times }
sum_set3 = { tup[0] + sum(tup[1]) for tup in cases_3times } # int + tuple이라서 오류가 발생한다.
sum_set3_recursive = { sum_set_recursive(tup, 3) for tup in cases_3times }
sum_set4_recursive = { sum_set_recursive(tup, 4) for tup in cases_4times }
sum_list4_recursive = [ sum_set_recursive(tup, 4) for tup in cases_4times ]
sum_set5_recursive = { sum_set_recursive(tup, 5) for tup in cases_5times }
sum_list5_recursive = [ sum_set_recursive(tup, 5) for tup in cases_5times ]

print(sum_set2)
print(sum_set3)
print(sum_set4_recursive)
print(sum_set5_recursive)
print(len(sum_list4_recursive))
print(len(sum_list5_recursive))