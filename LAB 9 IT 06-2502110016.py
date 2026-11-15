import os
import csv
from datetime import datetime

folder = "data"
output = "output"

os.makedirs(folder, exist_ok=True)
os.makedirs(output, exist_ok=True)


# Function to process individual files
def read_and_process(path):

    accepted = []
    rejected = []

    with open(path, "r") as file:
        lines = file.readlines()

    for line in lines:

        line = line.strip()

        try:
            code, qty, material = line.split(",")

            if not code.startswith("PART-"):
                raise ValueError("Invalid part code")

            if not qty.isdigit():
                raise ValueError("Invalid quantity format")

            qty = int(qty)

            if qty <= 0:
                raise ValueError("Quantity must be positive")

            if not material.strip():
                raise ValueError("Material missing")

            accepted.append([code, qty, material.strip()])

        except ValueError as error:
            rejected.append([line, str(error)])

    return lines, accepted, rejected


# Batch processing
all_records = 0
all_valid = 0
all_rejected = 0
plant_quantity = 0

history = []

for filename in os.listdir(folder):

    if filename.endswith(".txt"):

        filepath = os.path.join(folder, filename)

        lines, valid, invalid = read_and_process(filepath)

        quantity = sum(item[1] for item in valid)

        all_records += len(lines)
        all_valid += len(valid)
        all_rejected += len(invalid)
        plant_quantity += quantity

        # Generate individual report
        report_path = os.path.join(
            output,
            filename.replace(".txt", "_report.txt")
        )

        with open(report_path, "w") as report:

            report.write("FILE PRODUCTION REPORT\n")
            report.write("======================\n")

            report.write("Filename: " + filename + "\n")
            report.write("Total records: " + str(len(lines)) + "\n")
            report.write("Accepted: " + str(len(valid)) + "\n")
            report.write("Rejected: " + str(len(invalid)) + "\n")
            report.write("Total quantity: " + str(quantity) + "\n")

            report.write("\nVALID RECORDS\n")

            for item in valid:
                report.write(str(item) + "\n")

        history.append([
            filename,
            len(lines),
            len(valid),
            len(invalid)
        ])

        print("Completed:", filename)


# Combined plant summary
with open(
    os.path.join(output, "plant_summary.txt"), "w"
) as summary:

    summary.write("PLANT PRODUCTION SUMMARY\n")
    summary.write("========================\n")

    summary.write("Total records: " + str(all_records) + "\n")
    summary.write("Accepted: " + str(all_valid) + "\n")
    summary.write("Rejected: " + str(all_rejected) + "\n")
    summary.write("Production quantity: " + str(plant_quantity) + "\n")


# Append run history
history_path = os.path.join(output, "run_history.csv")

new_file = not os.path.exists(history_path)

with open(history_path, "a", newline="") as file:

    writer = csv.writer(file)

    if new_file:
        writer.writerow([
            "Date and Time",
            "Filename",
            "Records Processed",
            "Accepted",
            "Rejected"
        ])

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for item in history:
        writer.writerow([current_time] + item)


# Final output
print("\n========== BATCH SUMMARY ==========")
print("Total files processed:", len(history))
print("Total records:", all_records)
print("Accepted records:", all_valid)
print("Rejected records:", all_rejected)
print("Total production:", plant_quantity)

print("\nAll reports generated successfully!")
