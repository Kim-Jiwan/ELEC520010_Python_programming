# 2017110292 김지완

def removePunctuatios(string):
    
    punctuation = ['.', ',', '!', '?', ':', ';']
    
    for mark in punctuation:
        string = string.replace(mark, ' ')

    return string

string = input("여러 단어로 이루어진 글을 입력하세요 : ")

string = removePunctuatios(string) # punctuation 제거
string = string.split()            # 문자열 분리 후 리스트로 저장
string.sort()                      # 사전 배열 순서로 정렬

print("정렬 결과 : \n{}".format(string))