# 10 messy log lines
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

# Three separate bins
accepted = []
rework = []
scrap = []

# Store the part codes that are scrapped
scrap_parts = []

# Parse and classify each log
for line in logs:
    parts = line.split()

    part_code = parts[0]
    diameter = float(parts[1])

    # Example diameter rules:
    # 22 <= diameter <= 28: accepted
    # 20 <= diameter < 22 or 28 < diameter <= 30: rework
    # Otherwise: scrap
    if 22 <= diameter <= 28:
        accepted.append(diameter)

    elif 20 <= diameter < 22 or 28 < diameter <= 30:
        rework.append(diameter)

    else:
        scrap.append(diameter)
        scrap_parts.append(part_code)

# Counts
print("Accepted count:", len(accepted))
print("Rework count:", len(rework))
print("Scrap count:", len(scrap))

# Accepted average
if accepted:
    accepted_average = sum(accepted) / len(accepted)
    print("Accepted average:", accepted_average)
else:
    print("Accepted average: No accepted parts")

# Part codes that were scrapped
print("Scrapped part codes:", scrap_parts)
