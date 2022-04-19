# index 0 -> 0대, 1 -> 10대 ...
population_1 = (100, 150, 230, 120, 180, 100, 140, 95, 81, 21, 4)
population_2 = (300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1)

print(f"{sum(population_1[2:11])} {sum(population_2[2:11])}")

print(f"{sum(population_1[7:11]) / sum(population_1):.2f} {sum(population_2[7:11]) / sum(population_2)}")