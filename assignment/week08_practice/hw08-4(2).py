# 2017110292 김지완
with open("coord.txt", "r") as coords:
#coords = open("coord.txt", "r")

    coords_cnt = int(coords.readline().rstrip())
    coord_list = []

    for _ in range(coords_cnt):
        coord = coords.readline().rstrip()
        tmp = list(map(int, coord.split()))

        coord_list.append(tmp)

    coord_list_sorted = sorted(coord_list, reverse = False)

    with open("sortedcoord.txt", "w") as coords_sorted:
    # coords_sorted = open("sortedcoord.txt", "w")

        for coord in coord_list_sorted:
            x, y = str(coord[0]), str(coord[1])

            coords_sorted.write(f"{x} {y}\n")