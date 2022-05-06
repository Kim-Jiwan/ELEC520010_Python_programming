def sum_list(l):
    return sum(l)

def 

num_list = list(map(int, input("N개의 수를 입력하세요 : ").split()))

print(f"{sum(num_list)}")
print(f"{sum(num_list) / len(num_list)}")
print(f"{max(num_list)}")
print(f"{min(num_list)}")