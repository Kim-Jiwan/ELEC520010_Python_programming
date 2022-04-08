# 2017110292 김지완

s_list = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
not_empty_list = []

print(f"주어진 리스트 : {s_list}")

for element in s_list:
    if len(element) != 0:
        not_empty_list.append(element)

print(f"빈 원소를 제거한 결과 : {not_empty_list}")
