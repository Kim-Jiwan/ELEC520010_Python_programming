import random as rd

# f = open("randint30.txt", "w")

# for _ in range(30):
#     f.write(f"{rd.randint(1, 10)} ")

# f.close()

# with문을 쓰면 close() 없이 file open문을 사용할 수 있다.
# read하면 문자열을 반환한다!!
with open("randint30.txt", "r") as f:
    n = f.readline().rstrip()
    print(n.split())
    
    num_list = [ int(num) for num in list(map(int, f.readline().rstrip().split())) ]


    with open("randint30_count.txt", "w") as f1:
        for i in range(1, 11):
            f1.write(f"{i} : {num_list.count(i)}!!!\n")

