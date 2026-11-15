line = "P101, 24.98, DAY"

data = line.split(",")

code = data[0].strip()
dia = float(data[1].strip())
shift = data[2].strip()

print("Part Code:", code)
print("Diameter:", dia)
print("Shift:", shift)

print("Diameter + 0.01:", dia + 0.01)
