import os
import csv

os.makedirs("data", exist_ok=True)

source = "data/shift_log.txt"

# Create sample file if it does not exist
if not os.path.isfile(source):

    with open(source, "w") as f:
        f.write(
            "PART-201,10,Steel\n"
            "PART-202,20,Iron\n"
            "INVALID,30,Copper\n"
            "PART-203,-5,Wood\n"
            "PART-204,15,Plastic\n"
        )


good = []
bad = []

# Read file
with open(source, "r") as f:
    records = f.readlines()

# Parse and validate
for record in records:

    record = record.strip()

    try:
        code, qty, material = record.split(",")

        if not code.startswith("PART-"):
            raise ValueError("Incorrect part code")

        if not qty.isdigit():
            raise ValueError("Quantity must be numeric")

        qty = int(qty)

        if qty <= 0:
            raise ValueError("Invalid quantity")

        if material.strip() == "":
            raise ValueError("Material missing")

        good.append([code, qty, material.strip()])

    except ValueError as e:
        bad.append([record, str(e)])


# Aggregate data
total = sum(row[1] for row in good)
count = len(good)

average = total / count if count > 0 else 0


# Write production report
with open("data/report.txt", "w") as report:

    report.write("SHIFT PRODUCTION REPORT\n")
    report.write("=======================\n")

    report.write(f"Input records: {len(records)}\n")
    report.write(f"Valid records: {count}\n")
    report.write(f"Invalid records: {len(bad)}\n")
    report.write(f"Total quantity: {total}\n")
    report.write(f"Average quantity: {average:.2f}\n")

    report.write("\nVALID JOBS\n")

    for row in good:
        report.write(
            f"{row[0]} | {row[1]} | {row[2]}\n"
        )


# Write rejected records to CSV
with open("data/rejects.csv", "w", newline="") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow(["Rejected Record", "Reason"])

    for row in bad:
        writer.writerow(row)


print("Pipeline executed successfully!")
print("Report file created.")
print("Rejects CSV created.")
print("Valid records:", count)
print("Rejected records:", len(bad))
