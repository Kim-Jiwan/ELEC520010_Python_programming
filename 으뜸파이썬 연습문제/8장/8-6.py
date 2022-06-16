f = open("number1to10.txt", "r")

num = int(input("몇 번째 라인? : "))

for i in range(num):
   n =  f.readline().rstrip()
   print(n)