def is_leaf_year(num):
    is_leaf = False

    if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
        is_leaf = True
    else:
        is_laef = False
    
    return is_leaf

year = int(input())

if is_leaf_year(year):
    print(1)
else:
    print(0)