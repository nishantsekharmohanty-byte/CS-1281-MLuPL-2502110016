class Machine:
    def __init__(self, name, model, limit):
        self.name = name
        self.model = model
        self.limit = limit
        self.running = False

    def __str__(self):
        return f"{self.name} - {self.model} (Limit: {self.limit})"

    def start(self):
        self.running = True
        return f"{self.name} started"


# Commission two machines
machine1 = Machine("Lathe", "L100", 500)
machine2 = Machine("Drill", "D200", 300)

# Print both nameplates
print(machine1)
print(machine2)

# Start only machine1
print(machine1.start())

# Prove states are independent
print("Machine 1 running:", machine1.running)
print("Machine 2 running:", machine2.running)
