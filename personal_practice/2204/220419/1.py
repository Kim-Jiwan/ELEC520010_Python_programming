src = input("src = ")
output = src[0]
count = 0

for char in src:
    if output[-1] == char:
        count += 1
    else:
        output += str(count) + char
        count = 1

output += str(count)

output_recover = ''

for i in range(0, len(output), 2):
    output_recover += (output[i] * int(output[i + 1]))

print(f"output = {output}")
print(f"output_recover = {output_recover}")