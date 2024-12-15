cur_pose = [0, 0]
start_pose = (0, 0)
direction = 0 # up, right, down, left

def move_sideways(row, move_left, cur_pose):
    exes = []
    increment = 1
    if move_left:
        increment = -1
    while cur_pose[1] < len(row) - 1 and cur_pose[1] > 0:
        if row[cur_pose[1] + increment] == "#":
            return (cur_pose, exes)
        else:
            row[cur_pose[1]] = "X"
            if cur_pose not in exes:
                exes.append(cur_pose.copy())
            cur_pose[1] += increment
    row[cur_pose[1]] = "X"
    if cur_pose not in exes:
        exes.append(cur_pose.copy())
    return ([-1, -1], exes)

def move_vertical(grid, move_up, cur_pose):
    exes = []
    increment = 1
    if move_up:
        increment = -1
    while cur_pose[0] < len(grid) - 1 and cur_pose[0] > 0:
        if grid[cur_pose[0] + increment][cur_pose[1]] == "#":
            return (cur_pose, exes)
        else:
            grid[cur_pose[0]][cur_pose[1]] = "X"
            if cur_pose not in exes:
                exes.append(cur_pose.copy())
            cur_pose[0] += increment
    grid[cur_pose[0]][cur_pose[1]] = "X"
    if cur_pose not in exes:
                exes.append(cur_pose.copy())
    return ([-1, -1], exes)

def has_loop(grid):
    cur_pose = [start_pose[0], start_pose[1]]
    direction = 0
    traversed_up = []
    traversed_down = []
    traversed_left = []
    traversed_right = []
    while cur_pose != [-1, -1]:
        if direction == 0:
            cur_pose, down = move_vertical(grid, True, cur_pose)
            overlap = [pos for pos in down if pos in traversed_down]
            if overlap != []:
                return True
            traversed_down.extend(down)
        elif direction == 1:
            cur_pos, right = move_sideways(grid[cur_pose[0]], False, cur_pose)
            overlap = [pos for pos in right if pos in traversed_right]
            if overlap != []:
                return True
            traversed_right.extend(right)
        elif direction == 2:
            cur_pose, up = move_vertical(grid, False, cur_pose)
            overlap = [pos for pos in up if pos in traversed_up]
            if overlap != []:
                return True
            traversed_up.extend(up)
        elif direction == 3:
            cur_pose, left = move_sideways(grid[cur_pose[0]], True, cur_pose)
            overlap = [pos for pos in left if pos in traversed_left]
            if overlap != []:
                return True
            traversed_left.extend(left)
        direction = (direction + 1) % 4
    return False
    

with open("day6_input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
grid = [list(row) for row in data]
all_exes = []

for i in range(len(data)):
    pos = data[i].find("^")
    if pos != -1:
        cur_pose[0] = i
        cur_pose[1] = pos
        start_pose = (i, pos)

while cur_pose != [-1, -1]:
    exes = []
    if direction == 0:
        cur_pose, exes = move_vertical(grid, True, cur_pose)
    elif direction == 1:
        cur_pose, exes = move_sideways(grid[cur_pose[0]], False, cur_pose)
    elif direction == 2:
        cur_pose, exes = move_vertical(grid, False, cur_pose)
    elif direction == 3:
        cur_pose, exes = move_sideways(grid[cur_pose[0]], True, cur_pose)
    all_exes.extend([ex for ex in exes if ex not in all_exes])
    direction = (direction + 1) % 4

count = 0
for ex in all_exes:
    print(ex)
    new_grid = [list(row) for row in data]
    new_grid[ex[0]][ex[1]] = '#'
    if (has_loop(new_grid)):
        count += 1

print(count)