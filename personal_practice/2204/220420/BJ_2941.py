string = input()
tmp = string
croa_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
croa_word_cnt = 0

for word in croa_word:
    if word in string:
        croa_word_cnt += string.count(word)
        string = string.replace(word, "|")

string = string.replace("|", "")
croa_word_cnt += len(string)

print(croa_word_cnt)
