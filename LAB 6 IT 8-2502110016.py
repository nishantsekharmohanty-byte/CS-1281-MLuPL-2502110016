
# IT8 - Version 2

# Production log data
log_data = [
    "P201,15",
    "P202,25",
    "P203,35",
    "P204,45",
    "P205,8",
    "P206,30"
]


# Build catalogue from log lines
def build_catalogue(logs):
    parts = {}

    for entry in logs:
        code, dia = entry.split(",")
        parts[code] = float(dia)

    return parts


# Tool 1: Search for a part
def lookup(catalogue, code):
    diameter = catalogue.get(code, None)

    if diameter is None:
        return "Unknown Part"

    return diameter


# Tool 2: Identify scrap parts
def scrap_codes(catalogue):
    return {
        code for code, dia in catalogue.items()
        if dia < 10 or dia > 40
    }


# Main program
if __name__ == "__main__":

    catalogue = build_catalogue(log_data)

    print("Complete Catalogue:")
    print(catalogue)

    print("\nPart Search:")
    print("P201:", lookup(catalogue, "P201"))
    print("P999:", lookup(catalogue, "P999"))

    print("\nScrap Components:")
    print(scrap_codes(catalogue))
