import random

accept = 0
rework = 0
scrap = 0

for i in range(100):
    diameter = random.uniform(24.90, 25.10)

    if 24.95 <= diameter <= 25.05:
        bin = "ACCEPT"
        accept += 1
    elif 24.90 <= diameter < 24.95 or 25.05 < diameter <= 25.10:
        bin = "REWORK"
        rework += 1
    else:
        bin = "SCRAP"
        scrap += 1

    print(f"Diameter: {diameter:.2f} -> {bin}")

print("\n--- SHIFT REPORT ---")
print(f"ACCEPT: {accept}")
print(f"REWORK: {rework}")
print(f"SCRAP: {scrap}")
print("\nSame code, ten times the work, zero extra effort.")
