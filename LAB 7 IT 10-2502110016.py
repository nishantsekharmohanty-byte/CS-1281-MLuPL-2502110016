
# IT10 - The Guarded Machine

class Machine:

    def __init__(self, name, max_speed):
        self.__name = name
        self.__max_speed = max_speed
        self.__parts = 0
        self.__jobs = 0

    # Validating operating method
    def operate(self, speed, quantity):

        if speed < 500 or speed > self.__max_speed:
            return "ERROR: Speed is outside the permitted range."

        if quantity <= 0:
            return "ERROR: Quantity must be positive."

        self.__parts += quantity
        self.__jobs += 1

        return f"{self.__name} operated successfully."

    # Status getter
    def status(self):
        return {
            "Machine": self.__name,
            "Maximum Speed": self.__max_speed,
            "Parts Produced": self.__parts,
            "Jobs Completed": self.__jobs
        }


# Create machine object
m1 = Machine("CNC-01", 3000)

# Valid operation
print(m1.operate(1500, 20))

# Invalid operations
print(m1.operate(4000, 10))
print(m1.operate(1200, -5))

# Display machine status
print("\nMachine Status:")
print(m1.status())

# Demonstrating private attribute bypass
m1._Machine__max_speed = 5000

print("\nAfter bypassing the guard:")
print(m1.operate(4000, 10))
print(m1.status())
