N = int(input())
nums = []
max_num, max_indx = 0, 0

for _ in range(N):
    nums.append(int(input()))

for i in range(N):
    if i == 0:
        max_num = nums[0]
        max_indx = 1
    else:
        if nums[i] > max_num:
            max_num = nums[i]
            max_indx = i + 1

print(max_num, max_indx)