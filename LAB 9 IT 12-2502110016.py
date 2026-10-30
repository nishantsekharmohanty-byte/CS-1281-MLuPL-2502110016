
import os

# Create the data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create test records, including three deliberately faulty ones
records = [
    "WO01 | Machine A | Normal operation",
    "WO02 | Machine B | Completed successfully",
    "WO03 | Machine C | Temperature stable",
    "WO04 | Machine D | Maintenance completed",
    "WO05 | Machine A | No issues reported",
    "WO06 | Machine B | Oil level checked",
    "WO07 | Machine C | Running normally",

    # Three deliberately filthy records
    "WO08 | Machine X | ERROR: Temperature = -9999",
    "WO08 | ??? | NULL | !!! | BROKEN DATA",
    "WO08 | Machine Z | Pressure = HIGHHIGHHIGH",

    "WO09 | Machine D | Inspection passed",
    "WO10 | Machine A | Operating normally",
    "WO11 | Machine B | Filter replaced",
    "WO12 | Machine C | Maintenance required",
    "WO13 | Machine D | Shift completed"
]

# Write records to the file
with open("data/shift_log.txt", "w") as file:
    for record in records:
        file.write(record + "\n")

# Read the file back
with open("data/shift_log.txt", "r") as file:
    lines = file.readlines()

# Print the records and line count
print("SHIFT LOG:")
for line in lines:
    print(line.strip())

print("\nTotal line count:", len(lines))
