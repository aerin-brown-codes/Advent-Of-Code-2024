with open("day2_input.txt", "r") as f:
    data = f.read()

reports = data.split("\n")
safe_count = 0

test = [0, 1, 2, 3]

def check_safe(report):
    ascending = report[0] < report[1]
    i = 1
    while i < len(report):
        a = report[i - 1]
        b = report[i]
        difference = abs(a - b)
        safe = (a < b) == ascending and difference >= 1 and difference <= 3
        i += 1
        if not safe:
            return False
    return True

for report in reports:
    report = report.split(" ")
    for i in range(len(report)):
        report[i] = int(report[i])
    
    if check_safe(report.copy()):
        safe_count += 1
        continue
    for i in range(len(report)):
        if i < (len(report) - 1) and check_safe(report[:i] + report[i + 1:]):
            safe_count += 1
            break
        elif check_safe(report[:-1]):
            safe_count += 1
            break

print(safe_count)
            