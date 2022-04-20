def user_sum(n_list):
    S = 0

    for n in n_list:
        S += n

    return S

def user_mean(n_list):
    return user_sum(n_list) / len(n_list)

def user_max(n_list):
    n_max = n_list[0]

    for n in n_list:
        if n > n_max:
            n_max = n

    return n_max

def user_min(n_list):
    n_min = n_list[0]

    for n in n_list:
        if n < n_min:
            n_min = n

    return n_min

num_list = list(map(int, input("N개의 수를 입력하세요 : ").split()))

print(f"합 : {user_sum(num_list)}")
print(f"평균 : {user_mean(num_list)}")
print(f"최댓값 : {user_max(num_list)}")
print(f"최솟값 : {user_min(num_list)}")