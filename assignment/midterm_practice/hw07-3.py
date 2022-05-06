def str_comp(string):
    output = string[0]
    cnt = 0

    for char in src:
        if char == output[-1]:
            cnt += 1
        else:
            output += str(cnt) + char
            cnt = 1

    output += str(cnt)
            
    return output
    
src = input("문자을 입력하세요 : ")
print(f"scr = '{src}'")
        
print(f"output = '{str_comp(src)}'")