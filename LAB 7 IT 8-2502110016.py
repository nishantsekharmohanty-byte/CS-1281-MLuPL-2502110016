class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.__speed = 0
        self.__jobs = 0
        self.__rejected = 0

    def operate(self, speed):
        if speed < 0 or speed > self.limit:
            self.__rejected += 1
            return "Rejected"
        self.__speed = speed
        self.__jobs += 1
        return "Accepted"

    def status(self):
        return {
            "machine": self.name,
            "jobs": self.__jobs,
            "rejected": self.__rejected,
            "last_speed": self.__speed
        }


machine = Machine("Lathe", 100)

logs = [
    "J01,50", "J02,80", "J03,120", "J04,60", "J05,90",
    "J06,110", "J07,40", "J08,70", "J09,130", "J10,55"
]

for line in logs:
    code, speed = line.split(",")
    result = machine.operate(int(speed))
    print(code, result)

print("\nShift Report:")
print(machine.status())
