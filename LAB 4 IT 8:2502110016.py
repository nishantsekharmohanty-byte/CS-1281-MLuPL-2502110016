import random

mode = input("Enter mode (halt/skip): ").lower()

accept = 0
rework = 0
scrap = 0
inspected = 0

for i in range(100):
    diameter = random.uniform(24.90, 25.10)
    inspected += 1

    if 24.95 <= diameter <= 25.05:
        bin = "ACCEPT"
        accept += 1

    elif 24.90 <= diameter < 24.95 or 25.05 < diameter <= 25.10:
        bin = "REWORK"
        rework += 1

    else:
        bin = "SCRAP"
        scrap += 1
        print(f"Diameter: {diameter:.2f} -> SCRAP")

        if mode == "halt":
            print("HALT MODE: Scrap detected. Batch stopped.")
            break
        elif mode == "skip":
            print("SKIP MODE: Scrap logged. Continuing batch.")
            continue

    print(f"Diameter: {diameter:.2f} -> {bin}")

print("\n--- SHIFT REPORT ---")
print(f"Mode: {mode.upper()}")
print(f"Inspected: {inspected}")
print(f"ACCEPT: {accept}")
print(f"REWORK: {rework}")
print(f"SCRAP: {scrap}")
