# IT12 Rough cut · Three Jigs warm-up

# 1. inspect(dia) → bin label
def inspect(dia):
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    else:
        return "Large"


# Test inspect()
print("inspect tests:")
print(inspect(5))
print(inspect(15))
print(inspect(25))


# 2. tally(labels) → count dictionary
def tally(labels):
    counts = {}
    for label in labels:
        if label in counts:
            counts[label] += 1
        else:
            counts[label] = 1
    return counts


# Test tally()
print("\ntally test:")
print(tally(["Small", "Medium", "Small", "Large", "Medium"]))


# 3. report(shift, counts) → formatted line
def report(shift, counts):
    return f"Shift {shift}: {counts}"


# Test report()
print("\nreport test:")
print(report("A", {"Small": 2, "Medium": 2, "Large": 1}))


# 4. Combine everything
print("\nCombined test:")

diameters = [5, 12, 8, 22, 15, 25]

labels = []
for dia in diameters:
    labels.append(inspect(dia))

counts = tally(labels)

print(report("A", counts))
