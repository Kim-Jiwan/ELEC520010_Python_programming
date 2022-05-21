# 2017110292 김지완

n_list = list(range(1, 101))
new_list = [ n for n in filter(lambda x : x % 6 == 0, n_list)]

print(f"new_list = {new_list}")