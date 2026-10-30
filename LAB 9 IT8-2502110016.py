
import re

# Regex pattern:
# 1. Work order must follow WO + digits
# 2. Machine name is the second field
# 3. Status is the third field
# 4. Allows any spacing around | separators

pattern = re.compile(
    r"^\s*(WO\d+)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*$"
)

def parse_record(line):
    # OLD VERSION: split-based parser
    # parts = [part.strip() for part in line.split("|")]
    # if len(parts) != 3:
    #     return None
    # return parts[0], parts[1], parts[2]

    # NEW VERSION: Regex parser
    match = pattern.fullmatch(line)

    if match:
        work_order, machine, status = match.groups()

        if machine.strip() and status.strip():
            return work_order, machine.strip(), status.strip()

    return None


# Read actual input from file
input_file = "data/shift_log.txt"

valid_records = []
rejected_records = []

with open(input_file, "r") as file:
    for line_number, line in enumerate(file, start=1):
        result = parse_record(line.strip())

        if result:
            valid_records.append(result)
        else:
            rejected_records.append((line_number, line.strip()))

# Display results
print("REGEX PARSER RESULTS")
print("--------------------")

print("Valid records:", len(valid_records))
print("Rejected records:", len(rejected_records))

print("\nAccepted records:")
for record in valid_records:
    print(record)

print("\nRejected records:")
for record in rejected_records:
    print(record)

# Test comparison note:
# Regex parser survived more spacing variations than split().
# Split parser was simpler but did not validate the WO code shape.
