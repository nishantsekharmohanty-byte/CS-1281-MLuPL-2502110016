# Self-testing parser

def parser(line):

    fields = line.split(",")

    if len(fields) != 3:
        raise ValueError("Wrong field count")

    code, qty, material = fields

    if not code.startswith("PART-"):
        raise ValueError("Invalid code")

    if not qty.isdigit():
        raise ValueError("Quantity must be numeric")

    if int(qty) <= 0:
        raise ValueError("Quantity must be positive")

    if not material.strip():
        raise ValueError("Material missing")

    return True


def run_tests():

    tests = [
        ("", False),
        ("PART-301,10,Steel", True),
        ("BAD-302,20,Iron", False),
        ("PART-303,-5,Wood", False),
        ("PART-304,abc,Copper", False),
        ("PART-305,0,Glass", False),
        ("PART-306,15", False),
        ("PART-307,20,", False)
    ]

    success = 0
    failure = 0

    print("\nSELF TESTING REPORT")
    print("------------------------------")

    for index, (line, expected) in enumerate(tests, 1):

        try:
            parser(line)
            actual = True

        except (ValueError, TypeError):
            actual = False

        if actual == expected:
            print("Test", index, ": PASS")
            success += 1

        else:
            print("Test", index, ": FAIL")
            failure += 1

    print("------------------------------")
    print("Passed:", success)
    print("Failed:", failure)
    print("Total:", len(tests))


run_tests()
