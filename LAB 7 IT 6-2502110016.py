class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.parts = 0
        self.busy = False

    def process(self, speed):
        if speed <= self.limit:
            self.parts += 1
            self.busy = True
            return True
        return False


machines = [
    Machine("Lathe", 100),
    Machine("Drill", 80),
    Machine("Mill", 120)
]

jobs = [50, 70, 90, 60, 110, 40, 100, 75, 115, 55]

for speed in jobs:
    machine = next((m for m in machines if not m.busy), None)

    if machine:
        machine.process(speed)

    for m in machines:
        m.busy = False

busiest = max(machines, key=lambda m: m.parts)

print("Plant Report")
for m in machines:
    print(m.name, ":", m.parts, "parts")

print("Plant total:", sum(m.parts for m in machines))
print("Busiest machine:", busiest.name)
