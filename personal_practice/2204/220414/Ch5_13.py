def std_dev(num_list):
    mean = sum(num_list) / len(num_list)
    list_dev_square = []

    for num in num_list:
        dev_square = (num - mean) ** 2
        list_dev_square.append(dev_square)

    sigma = (sum(list_dev_square) / len(list_dev_square)) ** 0.5

    return sigma

nums = list(map(int, input("10의 수를 입력하세요 : ").split()))

print(f"합 : {sum(nums)}")
print(f"평균 : {(sum(nums) / len(nums)):.1f}")
print(f"표준편차 : {std_dev(nums):.2f}")