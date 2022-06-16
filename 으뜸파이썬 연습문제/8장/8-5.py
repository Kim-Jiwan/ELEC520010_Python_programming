f = open("number1to10.txt", "w")

for i in range(1, 11):
    f.write(f"{i:2d}\n")

f.close()