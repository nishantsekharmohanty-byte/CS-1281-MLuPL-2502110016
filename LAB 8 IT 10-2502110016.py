# Parser certification with rejection details

def validate(data):
    values = data.split(",")

    if len(values) != 3:
        raise ValueError("Three fields required")

    part, quantity, material = values

    if not part.startswith("PART-"):
        raise ValueError("Part number is incorrect")

    if not quantity.isdigit():
        raise ValueError("Quantity is not an integer")

    quantity = int(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if not material.strip():
        raise ValueError("Material is blank")

    return {
        "part": part,
        "quantity": quantity,
        "material": material.strip()
    }


data = [
    "PART-201,40,Steel",
    "PART-202,25,Iron",
    "BAD-203,15,Copper",
    "PART-204,-8,Wood",
    "PART-205,abc,Plastic",
    "PART-206,12,Aluminium",
    "PART-207,0,Glass"
]

valid_data = []
rejected_data = []

for item in data:
    try:
        valid_data.append(validate(item))

    except ValueError as error:
        rejected_data.append({
            "line": item,
            "reason": str(error)
        })

# Calculate average safely
total = sum(item["quantity"] for item in valid_data)

average = total / len(valid_data) if valid_data else 0

# Report
print("\n========== PRODUCTION REPORT ==========")

print("Total input:", len(data))
print("Successful:", len(valid_data))
print("Rejected:", len(rejected_data))
print("Total quantity:", total)
print("Average quantity:", round(average, 2))

print("\nACCEPTED RECORDS")

for item in valid_data:
    print(item)

print("\nREJECTS TABLE")

print("{:<25} {}".format("BAD LINE", "REASON"))

for item in rejected_data:
    print("{:<25} {}".format(
        item["line"], item["reason"]
    ))
