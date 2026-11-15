
accept = 0
rework = 0
scrap = 0

for i in range(10):
    d = float(input("Enter diameter: "))

    if 9.5 <= d <= 10.5:
        print("ACCEPT")
        accept = accept + 1

    elif 9.0 <= d < 9.5 or 10.5 < d <= 11.0:
        print("REWORK")
        rework = rework + 1

    else:
        print("SCRAP")
        scrap = scrap + 1

print("\nFinal Inspection Report")
print("Accepted parts:", accept)
print("Rework parts:", rework)
print("Scrap parts:", scrap)
