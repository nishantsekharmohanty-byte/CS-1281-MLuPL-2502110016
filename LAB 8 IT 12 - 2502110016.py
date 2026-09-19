# Eight hostile inputs from the rig
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


def parser(line):
    # Current lab05 parser
    code, dia = line.split(",")
    return code, float(dia)


print("Hostile input test:")

for i, test in enumerate(hostile, 1):
    try:
        result = parser(test)
        print(f"Test {i}: PASS -> {result}")
    except Exception as e:
        print(f"Test {i}: KILLED -> {type(e).__name__}: {e}")
