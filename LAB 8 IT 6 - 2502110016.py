def parse(line):
    try:
        code, dia = line.split(",")
        dia = float(dia)

        if not code.startswith("P"):
            raise ValueError("invalid part code")

        if dia < 0 or dia > 100:
            raise ValueError("diameter out of range")

        return code, dia

    except ValueError:
        return None


def run_tests():
    hostile = [
        "",
        "ABC",
        "12,",
        ",25",
        "12,25,30",
        "abc,25",
        "P101,-5",
        "P101,999999"
    ]

    print("PASS/FAIL TABLE")
    print("-------------------------------")

    for i, line in enumerate(hostile, 1):
        result = parse(line)

        if result is None:
            print(f"Test {i}: PASS - rejected {line!r}")
        else:
            print(f"Test {i}: FAIL - accepted {line!r}")


run_tests()
