def pronanc(string):
    prona = [".", ",", ":", ";", "!", "?"]

    for i in prona:
        string = string.replace(i, " ")
    
    return string


string = input("임의의 문장을 입력 : ")
# string = string.split()
string = pronanc(string)
string = string.split()
string.sort()


print(string)