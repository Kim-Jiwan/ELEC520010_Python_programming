# 2017110292 김지완

def short_string(s_List):
    string_shortest = s_List[2] # 짧은 문자열이 저장되는지 확인하기 위해 s_list에서 가장 긴 문자열 저장

    for i in s_List:
        if len(i) < len(string_shortest): # 가장 먼저 나타나는 최소길이 문자열을 저장하기 위해 <= 이 아닌 <을 사용
            string_shortest = i

    return string_shortest

s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'oqp']

print(f"가장 길이가 짧은 문자열 : {short_string(s_list)}")