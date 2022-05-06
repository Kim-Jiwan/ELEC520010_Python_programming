string = input().upper()
char_list = list(set(string))
cnt_list = [ string.count(char) for char in char_list ]

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(char_list[max_index])