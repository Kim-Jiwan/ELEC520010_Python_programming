words = input().upper()
unique_words = list(set(words))
MAX = 0
MAX_word = ''
MAX_num = 0

for i in unique_words:
    tmp = words.count(i)

    if MAX < tmp:
        MAX_word = i
    elif MAX == tmp:
        MAX_num += 1

if MAX_num > 0:
    print("?")
else:
    print(MAX_word)