with open("day4_input.txt", "r") as f:
    data = f.read()

data = data.split("\n")
count = 0

data = [list(row) for row in data]

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        if data[y][x] == 'A':
            if (data[y+1][x+1] == 'M' and data[y - 1][x - 1] == 'S') or (data[y+1][x+1] == 'S' and data[y - 1][x - 1] == 'M'):
                if (data[y+1][x-1] == 'M' and data[y - 1][x + 1] == 'S') or (data[y+1][x-1] == 'S' and data[y - 1][x + 1] == 'M'):
                    count += 1
print(count)