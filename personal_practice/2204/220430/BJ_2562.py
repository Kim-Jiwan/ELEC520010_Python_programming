num_list = []

for _ in range(9):
    num_list.append(int(input()))

max_value = num_list[0]
max_index = 0

for i in range(9):
    if num_list[i] > max_value:
        max_value = num_list[i]
        max_index = i

print(max_value)
print(max_index + 1)