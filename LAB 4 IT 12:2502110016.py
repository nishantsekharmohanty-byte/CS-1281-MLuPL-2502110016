import random

print("TEN DIAMETERS")

for i in range(10):
    d = random.uniform(24.90, 25.10)
    d = round(d, 2)

    print("Part", i + 1, ":", d)
