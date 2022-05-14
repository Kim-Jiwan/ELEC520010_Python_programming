string = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for alpha in alphabet:
    if alpha not in string:
        print(-1, end = " ")
    else:
            print(string.index(alpha), end = " ")