def inspect(dia):
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    return "Large"


def lookup(catalogue, code):
    return catalogue.get(code, 0)


def scrap_codes(catalogue):
    return {code for code, dia in catalogue.items()
            if dia < 10 or dia > 20}


# Parsed log lines
logs = [
    "P101,12",
    "P102,25",
    "P103,8",
    "P104,15"
]

# Build {part_code: diameter}
catalogue = {}
for line in logs:
    code, dia = line.split(",")
    catalogue[code] = float(dia)

print("Catalogue:", catalogue)

print("Lookup P101:", lookup(catalogue, "P101"))
print("Lookup P999:", lookup(catalogue, "P999"))

print("Scrap codes:", scrap_codes(catalogue))
