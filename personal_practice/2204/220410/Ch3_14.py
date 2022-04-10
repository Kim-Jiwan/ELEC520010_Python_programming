word = input("알파벳을 입력하시오 : ")
vowel_list = list("aeiou")

if word in vowel_list:
    print(f"{word}는 모음입니다.")
else:
    print(f"{word}는 자음입니다.")