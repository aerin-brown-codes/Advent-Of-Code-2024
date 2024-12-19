with open("day9_input.txt", "r") as f:
    data = f.read().strip()

disk_map = [int(i) for i in list(data)]
blocks = []

for i in range(len(disk_map)):
    if i % 2 == 0: # block
        blocks.append((i // 2, disk_map[i], False)) #file number, # of blocks, touched
    else: # space
        blocks.append((-1, disk_map[i], False)) 
j = len(blocks) - 1
while j >= 0:
    block = blocks[j]
    if block[0] != -1 and not block[2]: # movable block, attempt to move
        for k in range(j):
            pos_space = blocks[k]
            swapped = False
            if pos_space[0] == -1 and pos_space[1] == block[1]: # perfect swap
                blocks[k] = (block[0], block[1], True)
                swapped = True
            elif pos_space[0] == -1 and pos_space[1] > block[1]: # imperfect swap
                blocks[k] = (block[0], block[1], True)
                blocks.insert(k + 1, (-1, pos_space[1] - block[1], False))
                pos_space = (-1, block[1], False)
                swapped = True
                j += 1
            if swapped: # combine adjacent blanks at position j
                if j < len(blocks) - 1 and blocks[j + 1][0] == -1:
                    pos_space = (-1, pos_space[1] + blocks[j + 1][1], False)
                    blocks.pop(j + 1)
                if j > 0 and blocks[j - 1][0] == -1:
                    pos_space = (-1, pos_space[1] + blocks[j - 1][1], False)
                    blocks.pop(j - 1)
                    j -= 1
                blocks[j] = pos_space
                break
    j -= 1
final_lst = []
for block in blocks:
    final_lst += [block[0]] * block[1]
total = 0
for i in range(len(final_lst)):
    if final_lst[i] != -1:
        total += final_lst[i] * i
print(total)
