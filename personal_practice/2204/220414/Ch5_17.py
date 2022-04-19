animals = ["dog", "cat", "tiger", "lion"]
print(animals)

animals.remove("dog")
animals.append("dog")
print(animals)

for animal in animals:
    print(f"I love {animal}")