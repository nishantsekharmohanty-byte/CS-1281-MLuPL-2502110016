
# IT10 - Version 2

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

    for name in labels:
        if name in result:
            result[name] += 1
        else:
            result[name] = 1

    return result


def report(shift, counts):
    total = sum(counts.values())
    return f"Shift {shift}: Production = {total}, Categories = {counts}"


def main():
    measurements = [12, 18, 22, 28, 34, 39, 45, 15]

    categories = [inspect(x) for x in measurements]

    production = tally(categories)

    final_report = report("B", production)

    print(final_report)


if __name__ == "__main__":
    main()
