def remove_punctuations(string):

    punctuation = [".", ",", "!", "?", ";", ":"]

    for punct in punctuation:
        string = string.replace(punct, " ")

    return string

source = input("여러 단어로 이루어진 글을 입력하세요 : ")

source = remove_punctuations(source)
source = source.split()
source.sort()

print(f"정렬 결과 :\n{source}")