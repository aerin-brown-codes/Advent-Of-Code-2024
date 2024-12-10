cur_pose = [0, 0]
direction = 0 # up, right, down, left

def move_sideways(row, move_left):
    increment = 1
    if move_left:
        increment = -1
    while cur_pose[1] < len(row) - 1 and cur_pose[1] > 0:
        if row[cur_pose[1] + increment] == "#":
            return cur_pose
        else:
            row[cur_pose[1]] = "X"
            cur_pose[1] += increment
    return [-1, -1]

def move_vertical(grid, move_up):
    increment = 1
    if move_up:
        increment = -1
    while cur_pose[0] < len(grid) - 1 and cur_pose[0] > 0:
        if grid[cur_pose[0] + increment][cur_pose[1]] == "#":
            grid[cur_pose[0]][cur_pose[1]] = "^"
            return cur_pose
        else:
            grid[cur_pose[0]][cur_pose[1]] = "X"
            cur_pose[0] += increment
    return [-1, -1]

with open("day6_input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
grid = [list(row) for row in data]

for i in range(len(data)):
    pos = data[i].find("^")
    if pos != -1:
        cur_pose[0] = i
        cur_pose[1] = pos

while cur_pose != [-1, -1]:
    if direction == 0:
        cur_pose = move_vertical(grid, True)
    elif direction == 1:
        cur_pose = move_sideways(grid[cur_pose[0]], False)
    elif direction == 2:
        cur_pose = move_vertical(grid, False)
    elif direction == 3:
        cur_pose = move_sideways(grid[cur_pose[0]], True)
    direction = (direction + 1) % 4

result = "\n".join(["".join(row) for row in grid])
count = result.count("X") + 1
print(count)