def punctuation(string):
    punct_list = [".", ",", "!", "?", ":", ";"]

    for punct in punct_list:
        string = string.replace(punct, " ")

    return string

string = input("여러 단어로 이루어진 글을 입력하세요 : ")
string = punctuation(string)
string = string.split()
string.sort()

print(f"정렬 결과:\n{string}")