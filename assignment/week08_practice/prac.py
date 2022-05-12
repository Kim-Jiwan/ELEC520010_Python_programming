from ast import excepthandler
import sys

success = True
fname = input("입력 파일명 : ")

try:
    f = open(fname, "r", encoding = "UTF-8")
    
except IOError:
    print("Could not read file : ", fname)
    success = False

except:
    print("Unexpected error : ", sys.exc_info()[0])
    success = False

if success:
    n = 1
    l = f.readline()

    while l:
        print(f"{n:3d}: {l}", end = "")
        n += 1
        l = f.readline()
    
    f.close()
print("\nfile access successful? :", success)