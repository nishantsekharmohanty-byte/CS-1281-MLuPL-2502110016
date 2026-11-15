# Custom exception handling

class MachineError(Exception):
    pass


def operate_machine(part, quantity):

    if not part.startswith("PART-"):
        raise MachineError("Invalid part number")

    if quantity < 1:
        raise MachineError("Insufficient quantity")

    print("Machine accepted:", part)


def main():

    work_orders = [
        ("PART-201", 20),
        ("PART-202", 15),
        ("WRONG-203", 10),
        ("PART-204", 0),
        ("PART-205", 30)
    ]

    for part, quantity in work_orders:

        try:
            operate_machine(part, quantity)

        except MachineError as error:
            print("Machine stopped this job:", error)

    print("\nAll work orders checked.")


if __name__ == "__main__":
    main()
