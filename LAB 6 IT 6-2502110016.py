def inspect(dia):
    if dia < 10:
        return "Small"
    elif dia < 20:
        return "Medium"
    return "Large"

def lookup(catalogue, code):
    return catalogue.get(code, 0)

def scrap_codes(catalogue):
    return {code for code, dia in catalogue.items() if dia < 10 or dia > 20}

def tally(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return counts

def report(shift, counts):
    return f"Shift {shift}: {counts}"

logs = ["P101,12", "P102,25", "P103,8", "P104,15"]
catalogue = {x.split(",")[0]: float(x.split(",")[1]) for x in logs}

labels = [inspect(dia) for dia in catalogue.values()]
counts = tally(labels)

print(report("A", counts))
print("Lookup P999:", lookup(catalogue, "P999"))
print("Scrap:", scrap_codes(catalogue))
