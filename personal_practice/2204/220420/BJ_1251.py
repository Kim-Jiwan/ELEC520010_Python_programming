word = input().lower()
word_list = []

# pivot 정하는거랑 비슷한 개념인것 같은데..
for i in range(len(word) - 2):
    for j in range(i + 1, len(word) - 1):
        for k in range(j + 1, len(word)):
            tmp = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            word_list.append(tmp)

print(min(word_list))