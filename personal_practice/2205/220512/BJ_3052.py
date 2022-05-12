modulo_set = set()

for _ in range(10):
    num = int(input())

    modulo_set.add(num % 42)
    
print(len(modulo_set))