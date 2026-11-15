import random

count = 0
consecutive = 0
limit = 500

while count < limit and consecutive < 5:

    d = round(random.uniform(24.90, 25.10), 2)
    count += 1

    print("Part", count, "Diameter:", d)

    if 24.95 <= d <= 25.05:
        print("ACCEPT")
        consecutive += 1

    elif 24.90 <= d < 24.95 or 25.05 < d <= 25.10:
        print("REWORK")
        consecutive = 0

    else:
        print("SCRAP")
        consecutive = 0

print("\nFINAL REPORT")
print("Total parts inspected:", count)
print("Consecutive ACCEPT:", consecutive)

if consecutive == 5:
    print("TARGET ACHIEVED!")
else:
    print("SAFETY LIMIT REACHED!")
