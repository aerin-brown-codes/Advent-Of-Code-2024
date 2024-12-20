with open("day10_input.txt", "r") as f:
    data = f.read().split("\n")

elevation_list = [[] for i in range(10)]
route_map = []
for i in range(len(data)):
    row = []
    for j in range(len(data[i])):
        elevation = int(data[i][j])
        if elevation == 9:
            elevation_list[9].append((i, j))
            row.append(1)
        else:
            elevation_list[elevation].append((i, j))
            row.append(0)
    route_map.append(row)

total = 0
for i in range(8, -1, -1):
    for coord in elevation_list[i]:
        x = coord[0]
        y = coord[1]
        routes = 0
        if x > 0:
            if (x - 1, y) in elevation_list[i + 1]:
                routes += route_map[x - 1][y]
        if x < len(data) - 1:
            if (x + 1, y) in elevation_list[i + 1]:
                routes += route_map[x + 1][y]
        if y > 0:
            if (x, y - 1) in elevation_list[i + 1]:
                routes += route_map[x][y - 1]
        if y < len(data[x]) - 1:
            if (x, y + 1) in elevation_list[i + 1]:
                routes += route_map[x][y + 1]
        route_map[x][y] = routes
        if i == 0:
            total += routes

print(total)