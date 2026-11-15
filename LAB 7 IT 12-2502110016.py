
# IT12 - The Drawing

class Machine:

    # Constructor
    def __init__(self, name, power, speed_limit):
        self.name = name
        self.power = power
        self.speed_limit = speed_limit
        self.parts = 0

    # Machine nameplate
    def __str__(self):
        return (
            f"Machine: {self.name}\n"
            f"Power: {self.power} kW\n"
            f"Maximum Speed: {self.speed_limit} RPM\n"
            f"Parts Produced: {self.parts}"
        )

    # Working method
    def operate(self, quantity):
        self.parts += quantity
        return f"{self.name} produced {quantity} parts."


# Commission two machines
machine1 = Machine("Lathe-01", 5, 2500)
machine2 = Machine("Milling-02", 7, 3000)

# Operate machines
print(machine1.operate(10))
print(machine2.operate(15))

# Display both nameplates
print("\nMACHINE 1")
print(machine1)

print("\nMACHINE 2")
print(machine2)

# Prove independent states
print("\nINDEPENDENCE TEST")
machine1.operate(5)

print("Machine 1 parts:", machine1.parts)
print("Machine 2 parts:", machine2.parts)
