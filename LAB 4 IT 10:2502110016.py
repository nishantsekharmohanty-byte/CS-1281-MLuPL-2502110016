import random

accept = 0
rework = 0
scrap = 0

for i in range(10):
    d = round(random.uniform(24.90, 25.10), 2)

    print("Diameter:", d)

    if 24.95 <= d <= 25.05:
        print("ACCEPT")
        accept += 1

    elif 24.90 <= d < 24.95 or 25.05 < d <= 25.10:
        print("REWORK")
        rework += 1

    else:
        print("SCRAP")
        scrap += 1

print("\nSHIFT REPORT")
print("Accepted:", accept)
print("Rework:", rework)
print("Scrap:", scrap)
