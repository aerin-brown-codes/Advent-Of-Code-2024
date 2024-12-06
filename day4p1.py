import regex as re

with open("day4_input.txt", "r") as f:
    data = f.read()


data = data.split("\n")
count = 0

#Horizontal search
for row in data:
    count += len(re.findall("XMAS", row, overlapped=True))
    count += len(re.findall("SAMX", row, overlapped=True))

data = [list(row) for row in data]
col_length = len(data)
row_length = len(data[0])

diagonals_a = [[] for i in range(col_length + row_length)]
diagonals_b = [[] for i in range(col_length + row_length)]

for col in range(len(data[0])):
    # Vertical search
    column = "".join([data[y][col] for y in range(len(data))])
    count += len(re.findall("XMAS", column, overlapped=True))
    count += len(re.findall("SAMX", column, overlapped=True))

    # Building diagonals
    for row in range(len(data)):
        diagonals_a[row + col].append(data[row][col])
        diagonals_b[col - row + col_length].append(data[row][col])

for diagonal in diagonals_a:
    diag_str = "".join(diagonal)
    count += len(re.findall("XMAS", diag_str, overlapped=True))
    count += len(re.findall("SAMX", diag_str, overlapped=True))

for diagonal in diagonals_b:
    diag_str = "".join(diagonal)
    count += len(re.findall("XMAS", diag_str, overlapped=True))
    count += len(re.findall("SAMX", diag_str, overlapped=True))

print(count)