# 2017110292 김지완

n_list = list(range(1, 101))
new_list = [ n for n in n_list if n % 6 == 0 ]

print(f"new_list = {new_list}")