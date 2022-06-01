from re import A


def flatten(arr):
    arr_result = []
    
    # for문처럼 큰 범위가 먼저 나와야 한다!! 두번째 for문의 num이 list에 들어가는 argument
    arr_result = [ num  for num_list in arr 
                        for num in num_list ]

    return arr_result

org_list = [[1, 2, 3 ,4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(flatten(org_list))