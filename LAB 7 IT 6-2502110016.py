
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

