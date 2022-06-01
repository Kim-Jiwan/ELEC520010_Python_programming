test_list = ["No. 224", "No. 587", "No. 29", "No. 37"]
num_list_1 = []

for No in test_list:
    num_list_1.append(int(No.split()[1]))

num_list_2 = [ int(num.split()[1]) for num in test_list ]

print(num_list_1)
print(num_list_2)