with open("day9_input.txt", "r") as f:
    data = f.read().strip()

disk_map = [int(i) for i in list(data)]
blocks = []

for i in range(len(disk_map)):
    if i % 2 == 0:
        blocks += [i // 2] * disk_map[i]
    else:
        blocks += "." * disk_map[i]

i = 0
while i < len(blocks):
    if blocks[i] == ".":
        j = len(blocks) - 1
        while blocks[j] == "." and j != i:
            j -= 1
        if j == i:
            break
        blocks = blocks[:i] + [blocks[j]] + blocks[i + 1:j]
    i += 1

total = 0
for i in range(len(blocks)):
    total += i * blocks[i]
print(total)