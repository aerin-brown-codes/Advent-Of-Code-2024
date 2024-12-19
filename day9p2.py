with open("day9_input.txt", "r") as f:
    data = f.read().strip()

disk_map = [int(i) for i in list(data)]
blocks = []

for i in range(len(disk_map)):
    if i % 2 == 0: # block
        blocks += [i // 2] * disk_map[i]
    else: # space
        blocks.append("." * disk_map[i])
