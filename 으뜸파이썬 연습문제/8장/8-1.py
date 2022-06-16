from asyncio import exceptions
from unittest import result


try:
    a, b = input("두 수를 입력하세요 : ").split()
    result = int(a) * int(b)

except Exception as exception:
    print("숫자 2개를 입력하세요\n", exception)

else:
    print(result)


try:
    c, d = input("두 수를 입력하세요 : ").split()
    result = int(c) / int(d)

except Exception as e:
    print(e)

else:
    print(result)

