# Hostile test inputs

hostile = [
    " ",
    "ITEM-101,10,Steel",
    "PART-ABC,20,Iron",
    "PART-102,-10,Copper",
    "PART-103,abc,Wood",
    "PART-104,0,Plastic",
    "PART-105,10",
    "PART-106,15,"
]

def check_record(data):
    fields = data.split(",")

    if len(fields) != 3:
        raise ValueError("Incorrect number of fields")

    part, amount, material = fields

    if not part.startswith("PART-"):
        raise ValueError("Wrong part number")

    if not amount.isdigit():
        raise ValueError("Quantity must be numeric")

    if int(amount) <= 0:
        raise ValueError("Quantity must be greater than zero")

    if material.strip() == "":
        raise ValueError("Material cannot be empty")

    return True


for number, item in enumerate(hostile, start=1):
    try:
        check_record(item)
        print("Test", number, "PASSED")
    except (ValueError, TypeError) as error:
        print("Test", number, "FAILED:", error)
