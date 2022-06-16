def partition(arr):
    pivot = arr[0]
    left, right = 1, len(arr) - 1
    
    while left + 1 < right:
        while arr[left] <= pivot: # pivot보다 큰 값이 나올 때 까지 읽음
            left += 1
        
        while arr[right] >= pivot: # pivot보다 작은 값이 나올 때 까지 읽음
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]
     
    arr[0], arr[left] = arr[left], arr[0]

    return arr

org = input()
# org_list = list(map(int, input().split()))
org_list = [ int(num) for num in org.split() ]
part_list = partition(org_list)

print(part_list)