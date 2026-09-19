accept = 0
rework = 0
scrap = 0

for i in range(10):
    diameter = float(input(f"Enter diameter of item {i + 1}: "))

    if 9.95 <= diameter <= 10.05:
        print("ACCEPT")
        accept += 1
    elif 9.90 <= diameter < 9.95 or 10.05 < diameter <= 10.10:
        print("REWORK")
        rework += 1
    else:
        print("SCRAP")
        scrap += 1

print("Final Report: ACCEPT =", accept, ", REWORK =", rework, ", SCRAP =", scrap)
