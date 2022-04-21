# 2017110292 김지완

a, b, c = map(int, input('세 정수를 입력하세오 :').split())

if b <= c and c <= a:
    print(b, c, a)

elif c <= b and b <= a:
    print(c, b, a)

elif a <= c and c <= b:
    print(a, c ,b)

elif c <= a and a <= b:
    print(c, a, b)

elif a <= b and b <= c:
    print(a, b, c)
    
elif b <= a and b <= c:
    print(b, a, c)