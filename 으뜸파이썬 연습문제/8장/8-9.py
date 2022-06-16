f = open("coord.txt", "r")

N = int(f.readline().rstrip())

coords = []

for _ in range(N):
    num = list(map(int, f.readline().rstrip().split()))
    coords.append(num)

coords = sorted(coords, reverse = False)

f = open("coord_sorted.txt", "a")

for coord in coords:
    x, y = coord[0], coord[1]

    f.write(f"{x} {y}\n")

f.close()