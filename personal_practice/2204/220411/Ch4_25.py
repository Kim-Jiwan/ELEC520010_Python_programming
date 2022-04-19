def toCap(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    string = string.upper()

    return string

s1 = "Kang Young Min"
s2 = " Kang Young-Min"
s3 = "Park Dong Min"
s4 = " Park Dong-Yun"

S1 = toCap(s1)
S2 = toCap(s2)
S3 = toCap(s3)
S4 = toCap(s4)

print(f"{s1}은 {S1}로 수정됨")
print(f"{s2}은 {S2}로 수정됨")
print(f"{s3}은 {S3}로 수정됨")
print(f"{s4}은 {S4}로 수정됨")

S1_N = S1.count("N")
S2_N = S2.count("N")
S3_N = S3.count("N")
S4_N = S4.count("N")

print(f"{S1} : {S1_N} 개의 N이 나타남")
print(f"{S2} : {S2_N} 개의 N이 나타남")
print(f"{S3} : {S3_N} 개의 N이 나타남")
print(f"{S4} : {S4_N} 개의 N이 나타남")