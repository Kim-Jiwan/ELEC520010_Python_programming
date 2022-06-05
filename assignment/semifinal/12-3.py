def partition(alist, start, end):
    pivot = alist[0]
    left = start
    right = end

    while left + 1 < right:
        while alist[left] < pivot:
            left += 1

        while alist[right] > pivot:
            right -= 1
        
        alist[left], alist[right] = alist[right], alist[left]

    else:
        alist[0], alist[left] = alist[left], alist[0]

    pivot_index = left

    return alist, pivot_index

def quick_sort(alist, start, end):

    if start < end:
        alist, pivot_index = partition(alist, start, end)
        quick_sort(alist, start, pivot_index - 1)
        quick_sort(alist, pivot_index + 1, end)

    return alist

org_list = [8, 5, 12, 34, 3, 2, 97, 23, 45]
A_list = [15, 22, 13, 27, 12, 10, 20, 25]
print(org_list)
print(partition(org_list, 1, len(org_list) - 1))