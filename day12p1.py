def get_value(i, j):
    area = 0
    perimeter = 0
    next_to_explore = [(i, j)]
    plot_letter = grid[i][j][0]
    while len(next_to_explore) != 0:
        next_next = []
        for plot in next_to_explore:
            x = plot[0]
            y = plot[1]
            area += 1
            perimeter += 4
            grid[x][y] = (grid[x][y][0], True)
            if x > 0:
                p = grid[x - 1][y]
                if p[0] == plot_letter:
                    perimeter -= 1
                    if not p[1]:
                        next_next.append((x - 1, y))
            if y > 0:
                p = grid[x][y - 1]
                if p[0] == plot_letter:
                    perimeter -= 1
                    if not p[1]:
                        next_next.append((x, y - 1))
            if x < len(grid) - 1:
                p = grid[x + 1][y]
                if p[0] == plot_letter:
                    perimeter -= 1
                    if not p[1]:
                        next_next.append((x + 1, y))
            if y < len(grid[x]) - 1:
                p = grid[x][y + 1]
                if p[0] == plot_letter:
                    perimeter -= 1
                    if not p[1]:
                        next_next.append((x, y + 1))
        next_to_explore = set(next_next)
    return area * perimeter
    

with open("day12_input.txt", "r") as f:
    data = f.read()

grid = [[(p, False) for p in list(row)] for row in data.split("\n")]

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not grid[i][j][1]:
            total += get_value(i, j)
print(total)