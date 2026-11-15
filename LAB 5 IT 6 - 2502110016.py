day_logs = [
    "P101, 24.98, DAY",
    "P102, 25.15, DAY",
    "P103, 24.85, DAY",
    "P104, 25.02, DAY",
    "P105, 25.20, DAY"
]

night_logs = [
    "P101, 25.15, NIGHT",
    "P102, 24.99, NIGHT",
    "P106, 24.80, NIGHT",
    "P107, 25.03, NIGHT",
    "P108, 25.01, NIGHT"
]

day_scrap = set()
night_scrap = set()

day_accept = 0
night_accept = 0

# DAY SHIFT
for line in day_logs:
    data = line.split(",")
    code = data[0].strip()
    dia = float(data[1].strip())

    if 24.95 <= dia <= 25.05:
        day_accept += 1
    elif dia < 24.90 or dia > 25.10:
        day_scrap.add(code)

# NIGHT SHIFT
for line in night_logs:
    data = line.split(",")
    code = data[0].strip()
    dia = float(data[1].strip())

    if 24.95 <= dia <= 25.05:
        night_accept += 1
    elif dia < 24.90 or dia > 25.10:
        night_scrap.add(code)

# ACCEPTANCE RATE
day_rate = (day_accept / len(day_logs)) * 100
night_rate = (night_accept / len(night_logs)) * 100

print("DAY SHIFT ACCEPT RATE:", day_rate, "%")
print("NIGHT SHIFT ACCEPT RATE:", night_rate, "%")

# SET COMPARISON
print("\nCOMMON SCRAP CODES:")
print(day_scrap & night_scrap)

print("\nDAY ONLY SCRAP:")
print(day_scrap - night_scrap)

print("\nNIGHT ONLY SCRAP:")
print(night_scrap - day_scrap)

