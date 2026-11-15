
# IT12 - Version 2

# Function 1: Classify diameter
def inspect(dia):
    if dia >= 10 and dia < 20:
        return "Small"
    elif dia >= 20 and dia < 30:
        return "Medium"
    elif dia >= 30 and dia <= 40:
        return "Large"
    else:
        return "Out of Spec"


# Function 2: Calculate category counts
def tally(labels):
    result = {}

    for item in set(labels):
        result[item] = labels.count(item)

    return result


# Function 3: Prepare shift report
def report(shift, counts):
    total = 0

    for value in counts.values():
        total += value

    return f"{shift} Shift: {total} parts produced - {counts}"


# Independent testing
if __name__ == "__main__":

    print("Inspection Results:")
    print(inspect(12))
    print(inspect(24))
    print(inspect(36))
    print(inspect(50))

    print("\nCategory Counts:")
    data = ["Small", "Large", "Medium",
            "Small", "Large", "Small"]

    summary = tally(data)
    print(summary)

    print("\nShift Report:")
    print(report("B", summary))
