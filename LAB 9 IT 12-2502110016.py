import os

folder = "data"

os.makedirs(folder, exist_ok=True)

shift_records = [
    "PART-201,12,Steel",
    "PART-202,18,Iron",
    "PART-203,25,Copper",
    "PART-204,30,Wood",
    "PART-205,15,Plastic",
    "PART-206,22,Glass",
    "PART-207,10,Aluminium",
    "PART-208,35,Steel",
    "PART-209,16,Iron",
    "PART-210,20,Copper",
    "PART-211,-10,Wood",
    "INVALID,25,Plastic",
    "PART-213,abc,Glass",
    "PART-214,40,Steel",
    "PART-215,28,Aluminium"
]

path = os.path.join(folder, "shift_log.txt")

# Write records
with open(path, "w") as log:

    for record in shift_records:
        log.write(record + "\n")

print("Shift log generated!")

# Read records
with open(path, "r") as log:

    content = log.readlines()

print("\nSHIFT LOG CONTENT")

for index, record in enumerate(content, 1):
    print(index, record.strip())

print("\nTotal records:", len(content))
