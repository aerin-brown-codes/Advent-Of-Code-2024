with open("day2_input.txt", "r") as f:
    data = f.read()

reports = data.split("\n")
safe_count = 0

for report in reports:
    report = report.split(" ")
    if len(report) < 2:
        continue
    ascending = int(report[0]) < int(report[1])
    safe = True
    i = 1
    while i < len(report) and safe:
        a = int(report[i - 1])
        b = int(report[i])
        difference = abs(a - b)
        safe = (a < b) == ascending and difference >= 1 and difference <= 3
        i += 1
    if safe:
        safe_count += 1

print(safe_count)
            