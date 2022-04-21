# 2017110292 김지완

word = input("문자열을 입력하시오 : ").lower().replace(" ", "")
# word = word.replace(" ", "")

word_reverse = ""

for i in range(len(word)):
    word_reverse += word[len(word) - i - 1]

if word == word_reverse:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")


# 2 문자열 슬라이싱을 활용하는 방법
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

string = input("문자열을 입력하시오 : ")

if is_palindrome(string):
    print("회문입니다.")