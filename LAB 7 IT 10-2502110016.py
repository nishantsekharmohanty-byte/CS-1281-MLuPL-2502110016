class Machine:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.__speed = 0

    def operate(self, speed):
        if speed < 0 or speed > self.limit:
            return f"Rejected: speed must be between 0 and {self.limit}"
        self.__speed = speed
        return f"{self.name} running at {speed}"

    def status(self):
        return self.__speed


machine = Machine("Lathe", 100)

print(machine.operate(60))
print(machine.status())

print(machine.operate(150))
print(machine.status())
