def flatten(arr):
    return [ num for num_list in arr 
                    for num in num_list ]

org_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_list = flatten(org_list)

print(new_list)