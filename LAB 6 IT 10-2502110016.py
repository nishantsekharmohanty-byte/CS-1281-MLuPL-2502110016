# Before refactoring: 24 lines
# After refactoring: 17 lines
# Difference: 7 lines saved

def inspect(dia):
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    return "Large"


def tally(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return counts


def report(shift, counts):
    return f"Shift {shift}: {counts}"


diameters = [5, 12, 8, 22, 15, 25]
labels = [inspect(d) for d in diameters]
counts = tally(labels)
print(report("A", counts))
