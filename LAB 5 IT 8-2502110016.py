logs = [
    "P101, 24.98, DAY",
    "P102, 25.02, DAY",
    "P103, 24.85, DAY",
    "P104, 25.06, DAY",
    "P105, 24.99, DAY",
    "P106, 25.15, DAY",
    "P107, 24.92, DAY",
    "P108, 25.04, DAY",
    "P109, 24.80, DAY",
    "P110, 25.00, DAY"
]

accepted = []
rework = []
scrap = []
scrap_codes = []

for line in logs:
    data = line.split(",")

    code = data[0].strip()
    dia = float(data[1].strip())

    if 24.95 <= dia <= 25.05:
        accepted.append(dia)

    elif 24.90 <= dia <= 25.10:
        rework.append(dia)

    else:
        scrap.append(dia)
        scrap_codes.append(code)

print("Accepted:", accepted)
print("Rework:", rework)
print("Scrap:", scrap)

print("\nCOUNTS")
print("Accepted:", len(accepted))
print("Rework:", len(rework))
print("Scrap:", len(scrap))

if len(accepted) > 0:
    print("Accepted Average:", sum(accepted) / len(accepted))
else:
    print("No accepted parts")

print("Scrapped Part Codes:", scrap_codes)
