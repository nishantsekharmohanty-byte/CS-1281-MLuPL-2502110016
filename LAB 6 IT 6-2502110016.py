
# shoptools.py - Version 2

def inspect(dia):
    if 10 <= dia < 20:
        return "Small"
    elif 20 <= dia < 30:
        return "Medium"
    elif 30 <= dia <= 40:
        return "Large"
    return "Out of Spec"


def tally(labels):
    result = {}

    for item in set(labels):
        result[item] = labels.count(item)

    return result


def report(shift, counts):
    total = sum(counts.values())

    return f"{shift} Shift | Produced: {total} | {counts}"
    
# main.py - Version 2

import shoptools

measurements = [14, 22, 32, 18, 25, 42]

labels = [shoptools.inspect(x) for x in measurements]

counts = shoptools.tally(labels)

print(shoptools.report("B", counts))

