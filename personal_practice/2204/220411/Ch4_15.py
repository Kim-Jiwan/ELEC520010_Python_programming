def my_sort(*nums):
    # 가변인자를 쓰면 tuple로 받는다 
    nums = list(nums)
    nums.sort()

    print(f"결과 : {nums}")

my_sort(45, 3, 4, 56, 6)
my_sort(9, 8, 7, 6, 5, 4, 3)