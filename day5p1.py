with open("day5_input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

updates = data[1].split("\n")
rules_data = data[0].split("\n")
rules = {}

for rule in rules_data:
    parts = rule.split("|")
    if parts[1] in rules:
        rules[parts[1]].append(parts[0])
    else:
        rules[parts[1]] = [parts[0]]

total = 0
for update in updates:
    pages = update.split(",")
    valid = True
    for i in range(len(pages)):
        if pages[i] in rules:
            for page in rules[pages[i]]:
                if page in pages and not page in pages[:i]:
                    valid = False
                    break
        if not valid:
            break
    if valid:
        total += int(pages[(len(pages) - 1)//2])

print(total)