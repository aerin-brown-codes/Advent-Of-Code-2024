def index_2d(lst, elem):
    for i in range(len(lst)):
        if elem in lst[i]:
            return (i, lst[i].index(elem))
    return (-1, -1)

with open("day8_input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
frequencies = set(list("".join("".join(data).split("."))))

nodes = []
visualize_grid = [list(row) for row in data]
for freq in frequencies:
    towers = []
    grid = [list(row) for row in data]
    while True:
        result = index_2d(grid, freq)
        if result == (-1, -1):
            break
        else:
            towers.append(result)
            grid[result[0]][result[1]] = '.'
    for a in range(len(towers)):
        tower_a = towers[a]
        for tower_b in towers[(a + 1):]:
            distance_v = tower_a[0] - tower_b[0]
            distance_h = tower_a[1] - tower_b[1]
            node_1 = (tower_a[0] + distance_v, tower_a[1] + distance_h)
            if node_1 not in nodes:
                if node_1[0] >= 0 and node_1[0] < len(grid):
                    if node_1[1] >= 0 and node_1[1] < len(grid[0]):
                        nodes.append(node_1)
                        visualize_grid[node_1[0]][node_1[1]] = '#'
            node_2 = (tower_b[0] - distance_v, tower_b[1] - distance_h)
            if node_2 not in nodes:
                if node_2[0] >= 0 and node_2[0] < len(grid):
                    if node_2[1] >= 0 and node_2[1] < len(grid[0]):
                        nodes.append(node_2)
                        visualize_grid[node_2[0]][node_2[1]] = '#'

print(len(nodes))