s_list = ["abc", "bcd", "abc", "abba", "cddc", "opq", "opq"]
new_s_list = []

for string in s_list:
    if string not in new_s_list:
        new_s_list.append(string)

print(new_s_list)