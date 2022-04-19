name = input("이름을 입력하세요 : ")

print(name[-3::])

if name[-3::] == "vic":
    print(f"안녕하세요? {name}님, 발칸반도")
else:
    print(f"안녕하세요? {name}님")