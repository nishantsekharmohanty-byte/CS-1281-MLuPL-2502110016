total = int(input("Enter total parts: "))
size = int(input("Enter box size: "))

boxes = total // size
loose = total % size

print("Full boxes =", boxes)
print("Loose parts =", loose)
print("Audit:", boxes, "*", size, "+", loose, "==", total, "->", boxes * size + loose == total)
