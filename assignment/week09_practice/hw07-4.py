# 2017110292 김지완
import random as rd

rsp = { 1 : "가위", 2 : "바위", 3 : "보" }

romeo = rsp[rd.randrange(1, 4)]
juliet = rsp[rd.randrange(1, 4)]

print(f"로미오의 승부 : {romeo}")
print(f"줄리엣의 승부 : {juliet}")

if romeo == juliet:
    print("비겼습니다.")
elif (romeo == "가위" and juliet == "보") or (romeo == "바위" and juliet == "가위") or (romeo == "보" and juliet == "바위"):
    print("로미오가 이겼습니다.")
elif (romeo == "보" and juliet == "가위") or (romeo == "가위" and juliet == "바위") or (romeo == "바위" and juliet == "보"):
    print("줄리엣이 이겼습니다.")