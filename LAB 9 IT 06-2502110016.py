
import os
import re
import csv
from datetime import datetime
from collections import defaultdict

# Folder and output paths
DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "run_history.csv")
PLANT_REPORT = os.path.join(DATA_DIR, "plant_summary.txt")

os.makedirs(DATA_DIR, exist_ok=True)

# Regex parser
pattern = re.compile(
    r"^\s*(WO\d+)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*$"
)


def parse_record(line):
    match = pattern.fullmatch(line.strip())

    if not match:
        return None

    work_order, machine, status = match.groups()

    if not machine.strip() or not status.strip():
        return None

    # Reject suspicious test data
    if "NULL" in status or "ERROR" in status:
        return None

    if "HIGHHIGHHIGH" in status:
        return None

    return work_order, machine.strip(), status.strip()


def process_file(file_path):
    valid_records = []
    rejected_records = []
    total_records = 0

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, start=1):
            total_records += 1

            record = parse_record(line)

            if record:
                valid_records.append(record)
            else:
                rejected_records.append(
                    (line_number, line.strip(), "Invalid record")
                )

    return valid_records, rejected_records, total_records


def write_report(file_name, records, rejected, total):
    report_name = os.path.splitext(file_name)[0] + "_report.txt"
    report_path = os.path.join(DATA_DIR, report_name)

    machine_counts = defaultdict(int)

    for work_order, machine, status in records:
        machine_counts[machine] += 1

    with open(report_path, "w") as file:
        file.write("SHIFT REPORT\n")
        file.write("=" * 65 + "\n")

        file.write(
            f"{'WORK ORDER':<15}{'MACHINE':<20}{'STATUS':<30}\n"
        )
        file.write("-" * 65 + "\n")

        for work_order, machine, status in records:
            file.write(
                f"{work_order:<15}{machine:<20}{status:<30}\n"
            )

        file.write("\nMACHINE SUMMARY\n")
        file.write("-" * 30 + "\n")

        for machine, count in sorted(machine_counts.items()):
            file.write(f"{machine:<20}{count:>5}\n")

        file.write("\nTOTALS\n")
        file.write(f"Records processed: {total}\n")
        file.write(f"Accepted records: {len(records)}\n")
        file.write(f"Rejected records: {len(rejected)}\n")

    # Separate reject file for each input
    reject_path = os.path.join(
        DATA_DIR,
        os.path.splitext(file_name)[0] + "_rejects.csv"
    )

    with open(reject_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Line Number", "Rejected Record", "Reason"])
        writer.writerows(rejected)

    return report_path


def update_history(file_name, processed, rejects):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(HISTORY_FILE)
    needs_header = not file_exists or os.path.getsize(HISTORY_FILE) == 0

    with open(HISTORY_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if needs_header:
            writer.writerow([
                "Timestamp",
                "File Name",
                "Records Processed",
                "Rejects"
            ])

        writer.writerow([
            timestamp,
            file_name,
            processed,
            rejects
        ])


# MAIN BATCH JOB
all_records = []
total_processed = 0
total_rejected = 0
processed_files = []

print("PLANT BATCH JOB")
print("=" * 40)

# Only process source .txt files, not generated reports
for file_name in sorted(os.listdir(DATA_DIR)):

    if not file_name.lower().endswith(".txt"):
        continue

    if file_name.lower().endswith("_report.txt"):
        continue

    file_path = os.path.join(DATA_DIR, file_name)

    print("\nProcessing:", file_name)

    records, rejected, total = process_file(file_path)

    # Individual report and reject file
    report_path = write_report(
        file_name, records, rejected, total
    )

    # Add to plant totals
    all_records.extend(records)

    total_processed += total
    total_rejected += len(rejected)

    processed_files.append(file_name)

    # Record this run in history
    update_history(file_name, total, len(rejected))

    print("Accepted:", len(records))
    print("Rejected:", len(rejected))
    print("Report:", report_path)


# COMBINED PLANT SUMMARY
plant_counts = defaultdict(int)

for work_order, machine, status in all_records:
    plant_counts[machine] += 1

with open(PLANT_REPORT, "w") as file:
    file.write("COMBINED PLANT SUMMARY\n")
    file.write("=" * 45 + "\n")

    file.write("Files processed: " + str(len(processed_files)) + "\n")
    file.write("Records processed: " + str(total_processed) + "\n")
    file.write("Accepted records: " + str(len(all_records)) + "\n")
    file.write("Rejected records: " + str(total_rejected) + "\n")

    file.write("\nMACHINE TOTALS\n")
    file.write("-" * 30 + "\n")

    for machine, count in sorted(plant_counts.items()):
        file.write(f"{machine:<20}{count:>5}\n")

print("\n" + "=" * 40)
print("BATCH JOB COMPLETED")
print("Files processed:", len(processed_files))
print("Total records:", total_processed)
print("Accepted:", len(all_records))
print("Rejected:", total_rejected)
print("Plant report:", PLANT_REPORT)
print("Run history:", HISTORY_FILE)
