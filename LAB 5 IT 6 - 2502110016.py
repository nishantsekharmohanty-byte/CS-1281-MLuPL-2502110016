# Day-shift log lines
day_logs = [
    "P101   25.4   ACCEPT",
    "P102  30.2   SCRAP",
    "P103    18.7   SCRAP",
    "P104 22.5   ACCEPT",
    "P105     27.8   REWORK",
    "P106  31.0 SCRAP",
    "P107   19.6   SCRAP",
    "P108  24.3   ACCEPT",
    "P109 29.7   REWORK",
    "P110    21.5   ACCEPT"
]

# Night-shift log lines
night_logs = [
    "P101  25.4 ACCEPT",
    "P102    30.2 SCRAP",
    "P103 18.7 SCRAP",
    "P111   23.5 ACCEPT",
    "P112  31.5 SCRAP",
    "P113    27.2 REWORK",
    "P114 19.2 SCRAP",
    "P108   24.3 ACCEPT",
    "P115 29.5 REWORK",
    "P116  21.8 ACCEPT"
]


def parse_shift(logs):
    """Parse one shift and return total parts, accepted count, and scrap codes."""
    accepted_count = 0
    scrap_codes = []

    for line in logs:
        parts = line.split()

        part_code = parts[0]
        status = parts[2]

        if status == "ACCEPT":
            accepted_count += 1
        elif status == "SCRAP":
            scrap_codes.append(part_code)

    return len(logs), accepted_count, scrap_codes


# Parse day and night separately
day_total, day_accepted, day_scrap = parse_shift(day_logs)
night_total, night_accepted, night_scrap = parse_shift(night_logs)

# Calculate accept rates
day_accept_rate = day_accepted / day_total * 100
night_accept_rate = night_accepted / night_total * 100

print("DAY SHIFT")
print("Accept rate:", day_accept_rate, "%")
print("Scrap codes:", day_scrap)

print("\nNIGHT SHIFT")
print("Accept rate:", night_accept_rate, "%")
print("Scrap codes:", night_scrap)


# Convert scrap lists to sets for comparison
day_scrap_set = set(day_scrap)
night_scrap_set = set(night_scrap)

# Parts scrapped in BOTH shifts
scrapped_both = day_scrap_set & night_scrap_set

# Parts unique to the day shift
day_only_scrap = day_scrap_set - night_scrap_set

# Parts unique to the night shift
night_only_scrap = night_scrap_set - day_scrap_set

print("\nSCRAP COMPARISON")
print("Scrapped in both shifts:", sorted(scrapped_both))
print("Scrapped only during day:", sorted(day_only_scrap))
print("Scrapped only during night:", sorted(night_only_scrap))
