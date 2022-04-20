def is_group_word(word):
    isGroup = True

    for index in range(len(word) - 1):
        # 나왔던 문자가 연속하지 않게 또 나오면 -> isGroup = Fasle
        if word[index] != word[index + 1]:
            if word[index + 1] in word[:index]:
                isGroup = False

    return isGroup

N = int(input())
group_word_cnt = 0

for i in range(N):
    word = input()
    
    if is_group_word(word):
        group_word_cnt += 1

print(group_word_cnt)