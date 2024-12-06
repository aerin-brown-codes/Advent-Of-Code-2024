def create_update(pages, rules):
    if len(pages) <= 1:
        return pages
    for k, v in rules.items():
        if len(v) == 0:
            pages.remove(k)
            new_rules = {}
            for page in pages:
                new_rules[page] = [p for p in rules[page] if p in pages]
            return [k] + create_update(pages, new_rules)


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
    specific_rules = {}
    for i in range(len(pages)):
        if pages[i] in rules:
            specific_rules[pages[i]] = [page for page in rules[pages[i]] if page in pages]
            for page in rules[pages[i]]:
                if page in pages and not page in pages[:i]:
                    valid = False
        else:
            specific_rules[pages[i]] = []
    if not valid:
        new_update = create_update(pages, specific_rules)
        total += int(new_update[(len(new_update) - 1)//2])

print(total)