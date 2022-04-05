def group_word_checker(Word):
    i = 0
    is_group_word = True

    while i < len(Word):
        tmp = Word[i]


    return is_group_word

N = int(input())
cnt_group_word = 0
word = []

for _ in range(N):
    word.append(input())

for i in word:
    if group_word_checker(i):
        cnt_group_word += 1

print(cnt_group_word)
