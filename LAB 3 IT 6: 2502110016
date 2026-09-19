accept = 0
rework = 0
scrap = 0

# Batch inspection
for i in range(10):
    diameter = float(input(f"Enter diameter of part {i + 1}: "))

    if 9.95 <= diameter <= 10.05:
        print("ACCEPT")
        accept += 1
    elif 9.90 <= diameter < 9.95 or 10.05 < diameter <= 10.10:
        print("REWORK")
        rework += 1
    else:
        print("SCRAP")
        scrap += 1

# Pack only accepted parts into boxes of 4
box_size = 4
boxes = accept // box_size
loose = accept % box_size

# Closing summary
print("\n----- SHIFT SUMMARY -----")
print("Accepted Parts :", accept)
print("Rework Parts   :", rework)
print("Scrap Parts    :", scrap)
print("Full Boxes     :", boxes)
print("Loose Parts    :", loose)
print("Audit:", boxes, "*", box_size, "+", loose, "==", accept, "->", boxes * box_size + loose == accept)
