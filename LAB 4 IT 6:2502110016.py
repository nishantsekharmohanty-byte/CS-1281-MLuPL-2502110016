import random

consecutive_accepts = 0
attempts = 0
max_attempts = 500

while consecutive_accepts < 5 and attempts < max_attempts:
    diameter = random.uniform(24.90, 25.10)
    attempts += 1

    if 24.95 <= diameter <= 25.05:
        result = "ACCEPT"
        consecutive_accepts += 1
    else:
        result = "REWORK"
        consecutive_accepts = 0

    print(f"Part {attempts}: {diameter:.2f} -> {result} | Consecutive ACCEPTs: {consecutive_accepts}")

if consecutive_accepts == 5:
    print("\nSUCCESS: Five consecutive ACCEPTs achieved.")
    print(f"Parts required: {attempts}")
else:
    print("\nSAFETY STOP: Maximum attempts reached.")
    print(f"Parts inspected: {attempts}")

print("\nRECORD:")
print("An industrial program uses a safety cap so that an unexpected condition, faulty sensor, bad input, or endless process cannot make the machine run indefinitely.")
