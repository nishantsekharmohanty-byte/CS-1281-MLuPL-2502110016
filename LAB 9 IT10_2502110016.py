
import os
import csv

# File paths
input_file = "data/shift_log.txt"
report_file = "data/report.txt"
rejects_file = "data/rejects.csv"

# Storage
valid_records = []
rejected_records = []

# Step 1: Read input file
with open(input_file, "r") as file:
    lines = file.readlines()

# Step 2: Parse and validate
for line_number, line in enumerate(lines, start=1):
    line = line.strip()

    if not line:
        rejected_records.append(
            (line_number, line, "Empty record")
        )
        continue

    parts = [part.strip() for part in line.split("|")]

    if len(parts) != 3:
        rejected_records.append(
            (line_number, line, "Incorrect number of fields")
        )
        continue

    work_order, machine, status = parts

    if not work_order.startswith("WO"):
        rejected_records.append(
            (line_number, line, "Invalid work order")
        )
        continue

    if not machine or machine == "???":
        rejected_records.append(
            (line_number, line, "Invalid machine name")
        )
        continue

    if not status or status == "NULL" or "ERROR" in status:
        rejected_records.append(
            (line_number, line, "Invalid status")
        )
        continue

    if "HIGHHIGHHIGH" in status:
        rejected_records.append(
            (line_number, line, "Invalid pressure value")
        )
        continue

    valid_records.append((work_order, machine, status))

# Step 3: Aggregate valid records
machine_counts = {}

for work_order, machine, status in valid_records:
    machine_counts[machine] = machine_counts.get(machine, 0) + 1

# Step 4: Write human-readable report
with open(report_file, "w") as file:
    file.write("SHIFT LOG REPORT\n")
    file.write("=" * 65 + "\n")
    file.write(
        f"{'WORK ORDER':<15}{'MACHINE':<20}{'STATUS':<30}\n"
    )
    file.write("-" * 65 + "\n")

    for work_order, machine, status in valid_records:
        file.write(
            f"{work_order:<15}{machine:<20}{status:<30}\n"
        )

    file.write("\nMACHINE SUMMARY\n")
    file.write("-" * 30 + "\n")

    for machine, count in machine_counts.items():
        file.write(f"{machine:<20}{count:>5}\n")

    file.write("\n")
    file.write(f"Total input records: {len(lines)}\n")
    file.write(f"Accepted records: {len(valid_records)}\n")
    file.write(f"Rejected records: {len(rejected_records)}\n")

# Step 5: Write rejected records to CSV
with open(rejects_file, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Line Number", "Rejected Record", "Reason"])

    writer.writerows(rejected_records)

# Step 6: Print completion summary
print("FULL PIPELINE COMPLETED")
print("-----------------------")
print("Input records:", len(lines))
print("Accepted records:", len(valid_records))
print("Rejected records:", len(rejected_records))
print("\nOutput files created:")
print(report_file)
print(rejects_file)
