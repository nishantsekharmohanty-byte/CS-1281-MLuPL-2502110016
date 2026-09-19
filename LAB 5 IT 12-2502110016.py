# Raw bench line
line = "P123 25.4 3.5"

# Extract the fields
part_code, dia, shift = line.split()

# Convert diameter to a real float
dia = float(dia)

# Print each value with a label
print("Part code:", part_code)
print("Diameter:", dia)
print("Shift:", shift)

# Prove diameter is a number
print("Diameter + 0.01:", dia + 0.01)
