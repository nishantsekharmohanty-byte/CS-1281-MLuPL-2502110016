import re

# Old split-based parsing:
# parts = line.split(",")

# New regex-based parsing
pattern = re.compile(
    r"^\s*(PART-\d{3})\s*,\s*(\d+)\s*,\s*([A-Za-z]+)\s*$"
)


def extract_record(line):

    result = pattern.search(line)

    if result is None:
        raise ValueError("Record format is incorrect")

    part, quantity, material = result.groups()

    return part, int(quantity), material


records = [
    "PART-201,10,Steel",
    " PART-202 , 20 , Iron ",
    "PART-203,15,Copper",
    "PART-204,30,Wood",
    "INVALID,10,Glass",
    "PART-205,abc,Plastic",
    "PART-206,-5,Iron",
    "PART-207,25,Aluminium"
]

print("REGEX PARSER OUTPUT")
print("---------------------------")

for line in records:

    try:
        part, quantity, material = extract_record(line)

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        print("Accepted:", part, quantity, material)

    except ValueError as error:
        print("Rejected:", line, "-", error)

print("\nRegex parsing completed.")
