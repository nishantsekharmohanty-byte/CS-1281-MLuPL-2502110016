logs = [
    "P101, 24.98, DAY",
    "P102, 25.02, DAY",
    "P103, 24.95, DAY",
    "P104, 25.06, DAY",
    "P105, 24.99, DAY",
    "P106, 25.01, DAY",
    "P107, 24.97, DAY",
    "P108, 25.04, DAY",
    "P109, 24.93, DAY",
    "P110, 25.00, DAY"
]

diameters = []

for line in logs:
    data = line.split(",")

    dia = float(data[1].strip())
    diameters.append(dia)

print("Diameters:", diameters)
print("Count:", len(diameters))
print("Average:", sum(diameters) / len(diameters))
print("Minimum:", min(diameters))
print("Maximum:", max(diameters))
