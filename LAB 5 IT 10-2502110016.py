# 10 log lines with messy spacing
logs = [
    "P101   25.4   A",
    "P102  30.2 B",
    "P103    18.7    C",
    "P104 22.5 D",
    "P105     27.8 E",
    "P106  31.0    F",
    "P107   19.6 G",
    "P108  24.3     H",
    "P109 29.7 I",
    "P110    21.5    J"
]

# One list to store all diameters
diameters = []

# Parse each log line
for line in logs:
    parts = line.split()

    part_code = parts[0]
    diameter = float(parts[1])
    shift = parts[2]

    diameters.append(diameter)

# Report the results
count = len(diameters)
average = sum(diameters) / count
minimum = min(diameters)
maximum = max(diameters)

print("Diameters:", diameters)
print("Count:", count)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)

# Justification:
# A list is used because we want to keep every diameter,
# including duplicate values, and preserve their order.
# A set would remove duplicate values and does not preserve
# the original order in the same way. 
