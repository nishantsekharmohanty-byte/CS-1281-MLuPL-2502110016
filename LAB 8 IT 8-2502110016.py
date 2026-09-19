id="q7w4az"
class SpecViolation(Exception):
    pass


class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.parts = 0

    def operate(self, speed):
        if speed < 0 or speed > self.limit:
            raise SpecViolation(
                f"{self.name}: speed {speed} is outside limit {self.limit}"
            )

        self.parts += 1
        return f"{self.name} processed job"


machines = [
    Machine("Lathe", 100),
    Machine("Drill", 80),
    Machine("Mill", 120)
]

jobs = [50, 90, 150, 60, 70, 110, 40]

for i, speed in enumerate(jobs, 1):
    machine = machines[(i - 1) % len(machines)]

    try:
        print(machine.operate(speed))
    except SpecViolation as error:
        print("REJECTED:", error)

print("\nFleet Report")
for machine in machines:
    print(machine.name, ":", machine.parts, "parts")
