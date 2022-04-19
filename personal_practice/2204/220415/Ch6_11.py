# 2017110292 김지완

s_list = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
not_empty_list = []

for data in s_list:
    if len(data) == 0:
        s_list.remove(data)

for data in s_list:
    if len(data) != 0:
        not_empty_list.append(data)

print(s_list)
print(not_empty_list)