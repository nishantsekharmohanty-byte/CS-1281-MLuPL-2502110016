hostile = [
    "",
    "ABC",
    "12,",
    ",25",
    "12,25,30",
    "abc,25",
    "P101,-5",
    "P101,999999"
]

rejects = []
parts = []


def parse(line):
    try:
        code, dia = line.split(",")
        dia = float(dia)

        if dia < 0:
            raise ValueError("negative diameter")

        return code, dia

    except ValueError as e:
        rejects.append((line, str(e)))
        return None


for line in hostile:
    result = parse(line)

    if result is not None:
        parts.append(result)


# Guarded average
if parts:
    average = sum(dia for code, dia in parts) / len(parts)
else:
    average = 0


print("Report")
print("Valid parts:", len(parts))
print("Average diameter:", average)

print("\nRejects")
for line, reason in rejects:
    print(f"{line!r} -> {reason}")
