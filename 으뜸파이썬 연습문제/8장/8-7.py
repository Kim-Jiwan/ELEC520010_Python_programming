f1 = open("number1to10.txt", "r")
f2 = open("numberby10.txt", "w")

num = f1.readline().rstrip()

while num:
    f2.write(f"{int(num) * 10}\n")
    
    num = f1.readline().rstrip()

f1.close()
f2.close()

f1 = open("number1to10.txt", "r")
f2 = open("numberby10.txt", "r")
f3 = open("merge.txt", "w")

index = f1.readline().rstrip()
num = f2.readline().rstrip()

while index and num:
    f3.write(f"{int(index):2d} : {int(num)}\n")

    index = f1.readline().rstrip()
    num = f2.readline().rstrip()

f1.close()
f2.close()
f3.close()