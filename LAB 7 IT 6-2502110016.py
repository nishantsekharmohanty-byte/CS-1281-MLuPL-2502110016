
# shoptools.py

class Machine:

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.parts = 0
        self.jobs = 0
        self.free = True

    # Process an assigned job
    def operate(self, speed, quantity):

        if not self.free:
            return False

        if speed < 500 or speed > self.max_speed:
            return False

        if quantity <= 0:
            return False

        self.free = False

        self.parts += quantity
        self.jobs += 1

        self.free = True

        return True

    # Return machine status
    def status(self):
        return {
            "Machine": self.name,
            "Parts": self.parts,
            "Jobs": self.jobs,
            "Free": self.free
        }
        
# main.py

from shoptools import Machine

# Create three machines
machines = [
    Machine("Lathe-01", 3000),
    Machine("Milling-02", 3000),
    Machine("Drill-03", 3000)
]

# Production jobs: (speed, quantity)
jobs = [
    (1200, 10),
    (1500, 15),
    (2000, 12),
    (1800, 8),
    (2500, 20),
    (1000, 14),
    (2200, 16),
    (2800, 10),
    (1600, 18),
    (900, 12)
]

# Allocate jobs to available machines
next_machine = 0

for speed, quantity in jobs:

    assigned = False

    for step in range(len(machines)):

        index = (next_machine + step) % len(machines)

        machine = machines[index]

        if machine.status()["Free"]:

            if machine.operate(speed, quantity):
                print(
                    f"{quantity} parts assigned to "
                    f"{machine.name}"
                )

                next_machine = (index + 1) % len(machines)
                assigned = True
                break

    if not assigned:
        print("Job could not be assigned.")


# Plant production report
print("\nPLANT REPORT")

for machine in machines:
    print(machine.status())


# Calculate total plant production
total = sum(m.parts for m in machines)

print("\nTotal Plant Production:", total)


# Identify busiest machine
busiest = max(
    machines,
    key=lambda m: m.parts
)

print("Busiest Machine:", busiest.name)
print("Parts Produced:", busiest.parts)


