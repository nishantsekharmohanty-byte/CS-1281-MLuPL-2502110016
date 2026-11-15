
# IT8 - The Machine Runs a Batch

class Machine:

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.parts = 0
        self.jobs_completed = 0
        self.rejected_jobs = 0

    # Process one job
    def operate(self, job_id, speed, quantity):

        if speed < 500 or speed > self.max_speed:
            self.rejected_jobs += 1
            return f"{job_id}: Rejected - Invalid speed"

        if quantity <= 0:
            self.rejected_jobs += 1
            return f"{job_id}: Rejected - Invalid quantity"

        self.parts += quantity
        self.jobs_completed += 1

        return f"{job_id}: Successfully processed"

    # Return machine status
    def status(self):
        return {
            "Machine": self.name,
            "Completed Jobs": self.jobs_completed,
            "Rejected Jobs": self.rejected_jobs,
            "Total Parts": self.parts
        }


# Ten production jobs
job_logs = [
    "J01,1200,5",
    "J02,1800,4",
    "J03,3200,3",
    "J04,900,6",
    "J05,2500,2",
    "J06,400,5",
    "J07,1500,8",
    "J08,2800,3",
    "J09,2000,4",
    "J10,3500,2"
]


# Create machine
machine = Machine("CNC-01", 3000)

# Process batch
print("BATCH PROCESSING STARTED\n")

for line in job_logs:

    job_id, speed, quantity = line.split(",")

    result = machine.operate(
        job_id,
        int(speed),
        int(quantity)
    )

    print(result)


# Final shift report
print("\nSHIFT REPORT")
print(machine.status())
