src = input()
output = src[0]
count = 0

for char in src:
    if output[-1] == char:
        count += 1
    else:
        output += str(count) + char
        count = 1

output += str(count)

print(f"output = {output}")